#!/usr/bin/env python3
"""
strategy_backtest - 策略回测 Meta Skill
Atomic: historical OHLCV in → strategy logic → performance metrics out.
Composable with hhxg (data) and session-memory (logging).
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print(json.dumps({"error": "pandas required: pip install pandas"}))
    sys.exit(1)


def load_ohlcv(data_input) -> "pd.DataFrame":
    """Load OHLCV from CSV path or JSON string. Supports hhxg/akshare-like schema."""
    if isinstance(data_input, dict):
        df = pd.DataFrame(data_input)
    elif isinstance(data_input, str):
        s = data_input.strip()
        if s.startswith("{") or s.startswith("["):
            df = pd.DataFrame(json.loads(s))
        else:
            df = pd.read_csv(s)
    else:
        raise ValueError("data must be path (str) or JSON dict/list")

    # Normalize column names (AKShare/hhxg: 开盘, 收盘... → open, close...)
    col_map = {
        "开盘": "open", "开盘价": "open", "最高": "high", "最高价": "high",
        "最低": "low", "最低价": "low", "收盘": "close", "收盘价": "close",
        "成交量": "volume", "日期": "date", "datetime": "date",
    }
    df = df.rename(columns={c: col_map.get(c, str(c).lower().strip()) for c in df.columns})

    required = ["open", "high", "low", "close"]
    for c in required:
        if c not in df.columns:
            raise ValueError(f"Missing required column: {c}. Columns: {list(df.columns)}")

    if "volume" not in df.columns:
        df["volume"] = 0

    # Coerce OHLCV to numeric
    for c in ["open", "high", "low", "close", "volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["open", "high", "low", "close"])
    if df.empty:
        raise ValueError("No valid OHLCV rows after parsing")

    # Ensure index or date
    if "date" in df.columns and not isinstance(df.index, pd.DatetimeIndex):
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"]).set_index("date").sort_index()
    elif not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index, errors="coerce")
        df = df.dropna(how="all")
    df = df.sort_index()
    return df[["open", "high", "low", "close", "volume"]]


def run_sma_crossover(df: "pd.DataFrame", fast: int, slow: int) -> tuple:
    """SMA crossover backtest. Returns (equity_curve, trades)."""
    if fast >= slow:
        return pd.Series(dtype=float), []
    if len(df) < slow + 1:
        return pd.Series(dtype=float), []

    df = df.copy()
    df["sma_fast"] = df["close"].rolling(fast).mean()
    df["sma_slow"] = df["close"].rolling(slow).mean()
    df = df.dropna()

    # Signals
    df["signal"] = 0
    df.loc[df["sma_fast"] > df["sma_slow"], "signal"] = 1
    df.loc[df["sma_fast"] <= df["sma_slow"], "signal"] = -1
    df["position"] = df["signal"].diff().fillna(0)

    # Equity curve (simple: assume full position)
    df["returns"] = df["close"].pct_change()
    df["strategy_returns"] = df["returns"] * df["signal"].shift(1).fillna(0)
    df["equity"] = (1 + df["strategy_returns"]).cumprod()
    equity = df["equity"]

    # Trades with PnL
    trades = []
    entry_price = None
    for i in range(1, len(df)):
        pos = df["position"].iloc[i]
        if pos > 0:  # buy
            entry_price = float(df["close"].iloc[i])
            trades.append({"date": str(df.index[i]), "action": "buy", "price": entry_price})
        elif pos < 0 and entry_price is not None:  # sell
            exit_price = float(df["close"].iloc[i])
            pnl = (exit_price - entry_price) / entry_price
            trades.append({
                "date": str(df.index[i]),
                "action": "sell",
                "price": exit_price,
                "pnl": round(pnl, 4),
            })
            entry_price = None

    return equity, trades


def compute_metrics(equity: "pd.Series", trades: list) -> dict:
    """Compute performance metrics from equity curve and trades."""
    if equity.empty or len(equity) < 2:
        return {"error": "Insufficient data for backtest"}

    returns = equity.pct_change().dropna()
    e0, e1 = equity.iloc[0], equity.iloc[-1]
    total_return = 0.0
    if pd.notna(e0) and pd.notna(e1) and e0 != 0:
        total_return = float(e1 / e0 - 1)

    # Sharpe (annualized, assume daily data)
    if len(returns) > 0 and returns.std() != 0:
        sharpe = float(returns.mean() / returns.std() * (252 ** 0.5))
    else:
        sharpe = 0.0

    # Max drawdown
    cummax = equity.cummax()
    drawdown = (equity - cummax) / cummax.replace(0, np.nan)
    max_drawdown = float(drawdown.min()) if len(drawdown.dropna()) else 0.0

    # Win rate from sell trades
    sells = [t for t in trades if t.get("action") == "sell" and "pnl" in t]
    wins = sum(1 for t in sells if t["pnl"] > 0)
    win_rate = wins / len(sells) if sells else 0

    def safe_round(v):
        f = float(v) if v is not None else 0.0
        return round(f, 4) if np.isfinite(f) else 0.0

    return {
        "total_return": safe_round(total_return),
        "sharpe_ratio": safe_round(sharpe),
        "max_drawdown": safe_round(max_drawdown),
        "win_rate": safe_round(win_rate),
        "trade_count": len(trades),
        "trades": trades[:50],  # Limit for JSON size
    }


def main():
    parser = argparse.ArgumentParser(description="strategy_backtest - Quantitative backtest meta skill")
    parser.add_argument("--data", default="", help="CSV path or JSON string (OHLCV). Omit for demo.")
    parser.add_argument("--strategy", default="sma_crossover", help="Strategy type")
    parser.add_argument("--fast", type=int, default=5)
    parser.add_argument("--slow", type=int, default=20)
    parser.add_argument("--output", choices=["json", "print"], default="json")
    args = parser.parse_args()

    # Demo mode: use sample data when --data omitted (OpenClaw compatibility)
    data_input = args.data
    if not data_input:
        sample_path = Path(__file__).parent / "sample_ohlcv.csv"
        if sample_path.exists():
            data_input = str(sample_path)
            args.fast, args.slow = 3, 7  # Better for short sample
        else:
            print(json.dumps({"error": "No --data provided and sample_ohlcv.csv not found"}))
            sys.exit(1)

    try:
        df = load_ohlcv(data_input)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    if args.strategy == "sma_crossover":
        equity, trades = run_sma_crossover(df, args.fast, args.slow)
    else:
        print(json.dumps({"error": f"Unknown strategy: {args.strategy}"}))
        sys.exit(1)

    metrics = compute_metrics(equity, trades)
    if "error" in metrics:
        print(json.dumps(metrics))
        sys.exit(1)

    if args.output == "print":
        print("✅ Backtest complete")
        for k, v in metrics.items():
            if k != "trades":
                print(f"  {k}: {v}")
    else:
        print(json.dumps(metrics, indent=2))


def run_backtest(data_input, strategy="sma_crossover", fast=5, slow=20) -> dict:
    """
    Programmatic API for OpenClaw / session-memory integration.
    Returns metrics dict (JSON-serializable).
    """
    df = load_ohlcv(data_input)
    if strategy == "sma_crossover":
        equity, trades = run_sma_crossover(df, fast, slow)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
    return compute_metrics(equity, trades)


if __name__ == "__main__":
    main()

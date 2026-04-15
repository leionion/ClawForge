---
name: strategy-backtest
description: "Runs SMA crossover backtests on historical OHLCV/candlestick data, calculating total return, Sharpe ratio, max drawdown, win rate, and trade log. Supports CSV files and JSON input with automatic AKShare/hhxg column normalization. Use when the user asks to backtest a trading strategy, evaluate strategy performance on historical price data, run quantitative analysis, or mentions OHLCV, candlestick data, or equity curves."
---

# strategy-backtest — Quantitative Strategy Backtesting

Runs strategy backtests on historical OHLCV data and returns performance metrics as JSON. Supports SMA crossover strategy with configurable fast/slow periods.

## Usage

```bash
# Demo mode — uses built-in sample_ohlcv.csv
python3 strategy_backtest.py

# Backtest with custom CSV data
python3 strategy_backtest.py --data path/to/ohlcv.csv

# Backtest with JSON string input
python3 strategy_backtest.py --data '[{"open":10,"high":11,"low":9,"close":10.5,"volume":100}]'

# Custom SMA periods
python3 strategy_backtest.py --data prices.csv --fast 10 --slow 30

# Human-readable output
python3 strategy_backtest.py --data prices.csv --output print
```

## Parameters

| Flag | Default | Description |
|------|---------|-------------|
| `--data` | `sample_ohlcv.csv` | CSV path or JSON string (OHLCV) |
| `--strategy` | `sma_crossover` | Strategy type |
| `--fast` | `5` | Fast SMA period |
| `--slow` | `20` | Slow SMA period |
| `--output` | `json` | Output format (`json` or `print`) |

Supports column names in English (`open/high/low/close/volume`) or Chinese AKShare format (`开盘/收盘/最高/最低/成交量/日期`).

## Example output

```json
{
  "total_return": 0.0523,
  "sharpe_ratio": 1.2345,
  "max_drawdown": -0.0812,
  "win_rate": 0.6,
  "trade_count": 10,
  "trades": [
    {"date": "2024-01-15", "action": "buy", "price": 150.25},
    {"date": "2024-02-01", "action": "sell", "price": 158.50, "pnl": 0.0549}
  ]
}
```

## Error handling

- **Missing pandas**: prints `{"error": "pandas required: pip install pandas"}`
- **Missing columns**: reports which OHLCV columns are absent
- **Insufficient data**: returns error if fewer rows than the slow SMA window
- **Unknown strategy**: reports the unrecognized strategy name

## Programmatic API

```python
from strategy_backtest import run_backtest
metrics = run_backtest("prices.csv", strategy="sma_crossover", fast=5, slow=20)
```

## Related skills

- **hhxg-top-hhxg-python**: fetch A-share OHLCV data → feed into this skill
- **session-memory**: store backtest metrics for later comparison

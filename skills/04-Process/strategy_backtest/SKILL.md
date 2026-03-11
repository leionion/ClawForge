# strategy_backtest - 策略回测

**功能**: 对历史OHLCV数据运行策略回测，返回绩效指标。满足 Demand #3: Quantitative Stock Trading Skill (backtesting first).

**用法**:
```bash
# 演示模式 (无参数使用内置样本)
python3 strategy_backtest.py

# 指定数据
python3 strategy_backtest.py --data <path_or_json> [--strategy sma_crossover] [--fast 5] [--slow 20]
```

**输入**:
- `--data`: OHLCV 数据路径 (CSV) 或 JSON。可省略则使用 sample_ohlcv.csv 演示
- 支持列名: `open/high/low/close/volume` 或 AKShare/hhxg: `开盘/收盘/最高/最低/成交量/日期`
- `--strategy`: 策略类型，默认 `sma_crossover`
- `--fast`, `--slow`: SMA 周期 (sma_crossover)

**输出** (JSON，可传入 session-memory):
- `total_return`: 总收益率
- `sharpe_ratio`: 夏普比率
- `max_drawdown`: 最大回撤
- `win_rate`: 胜率
- `trade_count`: 交易次数
- `trades`: 交易列表

**与现有技能组合** (Related Skills):
- 数据: `hhxg-top-hhxg-python` (A 股 Niceck) → 输出 CSV/JSON → 本技能
- 历史: `session-memory` ← 本技能 metrics

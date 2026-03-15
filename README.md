# ⚡ ClawForge

**AI Trading Platform — Skill Forge, Chat, BankrBot, Polyclaw, Alpaca, Kalshi, Whale Tracking, Portfolio. Powered by OpenClaw.**

ClawForge bridges natural language and executable AI capabilities. Describe what you want — backtest a strategy, backup memory, automate workflows, trade across stocks and crypto — and get it done with **OpenClaw** agents and the **Skill Forge** demand decomposition engine.

---

## 🖥️ Demo

<p align="center">
  <img src="media/web-dashboard.gif" alt="ClawForge Dashboard" width="800" />
</p>

*Skill Forge, Chat, BankrBot, Polyclaw, Alpaca, Whale Tracking, DCA, Price Alerts, Portfolio — one unified AI trading terminal.*

---

## 🎯 Our Mission

**We exist to collaborate with traders and developers to build customized AI trading agents and bots.**

Our goal is not just a product — it's a **shared platform** where:

- **Traders** automate strategies, backtest ideas, and deploy agents without deep coding
- **Developers** extend skills, integrate new exchanges, and ship custom agents fast
- **Everyone** benefits from a growing ecosystem of open, reusable AI capabilities

ClawForge is **actively developed** and designed for **collaboration**. We want to **work together** with you to build the AI trading tools you actually need.

---

## ✨ What's Inside

| Area | Features |
|------|----------|
| **Skill Forge** | Decompose natural demands → atomic skills (keyword + Chutes LLM). Run locally or send to OpenClaw |
| **Chat** | Talk to your OpenClaw agent. Full tools, skills, memory. Fallback to direct Groq/Chutes when gateway is busy |
| **BankrBot** | Crypto spot, DeFi, 5 chains |
| **Polyclaw** | Polymarket prediction markets (CLOB) |
| **Alpaca** | US stocks, ETFs, options |
| **Kalshi** | CFTC prediction markets |
| **Whale Tracking** | On-chain intelligence, Base |
| **DCA** | Dollar Cost Averaging via crypto-trader |
| **Price Alerts** | Crypto alerts, Telegram/Discord |
| **Portfolio** | Cross-asset monitoring, drift detection, rebalancing |
| **Status** | OpenClaw CLI, Gateway, skills dashboard |

**Standalone skills:** `memory_backup`, `strategy_backtest` run without OpenClaw.  
**OpenClaw skills:** BankrBot, Polyclaw, DCA, Price Alerts use the OpenClaw gateway and ClawHub skills.

---

## 🚀 Quick Start

```bash
git clone https://github.com/leionion/ClawForge.git
cd ClawForge
pip install -e .
cp .env.example .env   # Add GROQ_API_KEY (free at console.groq.com)
streamlit run web_app.py --server.port 8503
```

**With OpenClaw (full agent):**
```bash
./scripts/setup_openclaw.sh
./scripts/start_gateway.sh   # or: pm2 start ecosystem.config.cjs
```

---

## 🗺️ Roadmap

### v0.3 (Current — Actively Developing)
- [x] Skill Forge with keyword + Chutes LLM decomposition
- [x] Chat with OpenClaw + direct LLM fallback
- [x] Gateway resilience (model fallbacks, env loading)
- [x] Trading pages: BankrBot, Polyclaw, Alpaca, Kalshi, Whale Tracking, DCA, Price Alerts, Portfolio
- [x] metaskillbase skill for OpenClaw
- [ ] More standalone skills (file ops, system)
- [ ] Improved error handling and diagnostics

### v0.4 (Next)
- [ ] Multi-agent routing (specialist agents per domain)
- [ ] Skill marketplace / ClawHub integration in UI
- [ ] Session persistence and history
- [ ] Webhook triggers for alerts and automation
- [ ] Custom skill builder (no-code templates)

### v0.5+
- [ ] Mobile-friendly PWA
- [ ] Plugin system for third-party skills
- [ ] Community skill registry and ratings
- [ ] Self-hosted and cloud deployment options
- [ ] API for external integrations

---

## 🤝 Let's Work Together

**Our total purpose is to collaborate with potential traders and developers to build customized AI agents and trading bots.**

Whether you want to:
- **Automate your strategies** with an AI agent
- **Build a custom trading bot** for your use case
- **Add new skills** or integrate new exchanges
- **Contribute** to the platform and roadmap

— we want to work with you.

**Reach out:** Visit our [GitHub profile](https://github.com/leionion) for Twitter, Telegram, and other social links. Open Issues, start Discussions, or DM — we respond to serious collaboration proposals and are open to new project ideas, skill contributions, and long-term partnerships.

---

## 🛠️ Tech Stack

- **Python 3.10+** — Core logic, skills, Cutter
- **Streamlit** — Web UI
- **OpenClaw** — Agent runtime, gateway, skills
- **Chutes / Groq** — LLM (decomposition, chat)
- **Pandas, NumPy** — Data (backtest, memory backup)

---

## 📁 Project Structure

```
ClawForge/
├── web_app.py           # Streamlit entry
├── core/
│   ├── cutter.py       # Demand decomposition (keyword + LLM)
│   ├── openclaw_gateway.py  # Chat completions, fallback
│   ├── openclaw_client.py   # CLI integration, invoke agent
│   ├── ui_components.py     # Theme, cards, sidebar
│   └── icons.py
├── pages/               # Streamlit pages (Skill Forge, Chat, BankrBot, …)
├── skills/              # Standalone skills (memory_backup, strategy_backtest, …)
├── openclaw-skill/      # metaskillbase skill for OpenClaw
├── scripts/             # Setup, gateway, fix
└── config.py, .env.example
```

---

## 📜 License

See [LICENSE](LICENSE) in the repo.

---

**ClawForge** — *AI Trading · OpenClaw · Built for Collaboration*

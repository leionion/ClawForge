# ⚡ ClawForge

**AI Trading Platform — Skill Forge, Chat, BankrBot, Polyclaw, Alpaca, Kalshi, Whale Tracking, Portfolio. Powered by OpenClaw.**

[![OpenClaw](https://img.shields.io/badge/OpenClaw-ECOSYSTEM-blue)](https://openclaw.ai)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://python.org)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)](https://streamlit.io)

ClawForge bridges natural language and executable AI capabilities. Describe what you want — backtest a strategy, backup memory, automate workflows, trade across stocks and crypto — and get it done with **OpenClaw** agents and the **Skill Forge** demand decomposition engine.

---

## 🎯 Vision

We are building the **default platform for customizable AI trading agents**. Our mission:

- **Democratize AI agent development** — Make it possible for traders and developers to build, extend, and deploy customized OpenClaw agents without deep infrastructure work
- **Unify trading workflows** — One interface for stocks, crypto, prediction markets, on-chain intelligence, and automation
- **Open collaboration** — Grow a community of contributors who build, share, and improve skills and agents together

ClawForge is not a closed product. It is an **actively developed open platform** designed for extension, contribution, and collaboration.

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

## 🤝 Collaborate With Us

We are **actively looking for collaborators** who want to build customized OpenClaw AI agents.

Whether you are a:
- **Trader** wanting to automate strategies
- **Developer** building new skills or agents
- **Researcher** exploring LLM-based decomposition
- **Contributor** fixing bugs or improving docs

— we want to hear from you.

### Get in Touch

| Platform | Link |
|----------|------|
| **GitHub** | [@leionion](https://github.com/leionion) |
| **Email** | j.ohnceballos0716@gmail.com |

**Have a mind to collaborate and build new customized AI agents together?**  
Reach out via GitHub (Issues, Discussions, or DM) or the links above. We respond to serious proposals and are open to new project ideas, skill contributions, and long-term collaboration.

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

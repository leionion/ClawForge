#!/usr/bin/env python3
"""ClawForge — AI Trading Platform."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, project_card_with_open_html, render_sidebar_nav
from core.icons import HERO_ICON

st.set_page_config(
    page_title="ClawForge",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_global_css()

# Sidebar first — ensure left panel renders
with st.sidebar:
    render_sidebar_nav()
    st.caption("AI Trading · OpenClaw · Groq")

# Hero
st.markdown(f"""
<div class="cf-hero">
  <h1><span class="cf-hero-icon">{HERO_ICON}</span>ClawForge</h1>
  <p class="sub">AI Trading Platform — Skill Forge, Chat, BankrBot, Polyclaw, Alpaca, Kalshi, Whale Tracking, Portfolio. Powered by OpenClaw.</p>
</div>
""", unsafe_allow_html=True)

# Card with Open button contained inside — whole card is clickable
def card_block(name, desc, icon_key, badge, page):
    st.markdown(project_card_with_open_html(name, desc, icon_key, badge, page), unsafe_allow_html=True)

st.markdown("#### Core Tools")
c1, c2, c3 = st.columns(3)
with c1:
    card_block("Skill Forge", "Decompose demands → skills. Chutes LLM.", "zap", "Chutes", "pages/1_Skill_Forge.py")
with c2:
    card_block("Chat", "Talk to OpenClaw agent. Full tools & skills.", "message", "Agent", "pages/2_Chat_with_OpenClaw.py")
with c3:
    card_block("BankrBot", "Crypto spot, DeFi, 5 chains.", "bot", "Bankr", "pages/3_BankrBot.py")

st.markdown("#### Trading & Markets")
c4, c5, c6, c7 = st.columns(4)
with c4:
    card_block("Polyclaw", "Polymarket prediction markets. CLOB.", "trending-up", "Chainstack", "pages/7_Polyclaw.py")
with c5:
    card_block("Alpaca", "US stocks, ETFs, options.", "bar-chart", "Alpaca", "pages/8_Alpaca.py")
with c6:
    card_block("Kalshi", "CFTC prediction markets.", "clipboard", "Read-only", "pages/9_Kalshi.py")
with c7:
    card_block("Whale Tracking", "On-chain intelligence.", "activity", "Base", "pages/10_Whale_Tracking.py")

st.markdown("#### Strategies & Alerts")
c8, c9, c10 = st.columns(3)
with c8:
    card_block("DCA", "Dollar Cost Averaging.", "wallet", "crypto-trader", "pages/4_DCA.py")
with c9:
    card_block("Price Alerts", "Crypto alerts. Telegram/Discord.", "bell", "price-tracker", "pages/5_Price_Alerts.py")
with c10:
    card_block("Portfolio", "Rebalancing, drift detection.", "folder", "Multi-asset", "pages/11_Portfolio.py")

st.markdown("#### System")
sc1, sc2, sc3 = st.columns([1, 1, 2])
with sc1:
    card_block("Status", "OpenClaw CLI, Gateway, skills.", "layout-dashboard", "Dashboard", "pages/6_Status.py")

render_footer()

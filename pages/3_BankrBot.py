"""BankrBot — Crypto balances, portfolio, trades via OpenClaw."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="BankrBot | ClawForge", page_icon="🦾", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("BankrBot", "Crypto spot, DeFi, 5 chains (Base, Ethereum, Polygon, Solana, Unichain). Swiss Army knife.", "🦾")

security_notice()

if not is_gateway_ready():
    st.info("Install Bankr skill: `clawhub install bankr` then start OpenClaw gateway.")
    onboarding_gateway()
    render_footer()
    st.stop()

presets = [
    "What is my ETH balance on Base?",
    "Show my portfolio on Binance",
    "Buy $10 of PEPE on Base",
    "What's my total portfolio value?",
]
choice = st.selectbox("Quick command", ["— Custom —"] + presets)
if choice == "— Custom —":
    cmd = st.text_input("Your command", placeholder="e.g. What is my ETH balance?")
else:
    cmd = choice

if cmd and st.button("Execute"):
    with st.spinner("BankrBot..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-bankrbot")
    if ok:
        st.success("Done")
        st.markdown(out[:2000] if out else "—")
    else:
        st.error(out[:300])
render_footer()

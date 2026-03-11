"""Whale Tracking — On-chain intelligence, whale alerts."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="Whale Tracking | ClawForge", page_icon="🐋", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Whale Tracking", "On-chain intelligence — new pairs, smart money, liquidity changes, token safety.", "🐋")

security_notice()

if not is_gateway_ready():
    st.info("Install: `clawhub install base-signal-feed` or whale-tracking skill.")
    onboarding_gateway()
    render_footer()
    st.stop()

presets = [
    "New trading pairs on Base",
    "Smart money activity on Base",
    "Large wallet movements in last 24h",
    "Token safety scores for trending tokens",
]
choice = st.selectbox("Quick command", ["— Custom —"] + presets, key="whale_cmd")
if choice == "— Custom —":
    cmd = st.text_input("Your command", placeholder="e.g. Whale buys of ETH in last 6 hours", key="whale_input")
else:
    cmd = choice

if cmd and st.button("Execute", key="whale_run"):
    with st.spinner("Scanning..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-whale")
    if ok:
        st.success("Done")
        st.markdown(out[:3000] if out else "—")
    else:
        st.error(out[:400])

st.markdown("---")
st.caption("Configure Telegram/Discord in OpenClaw for live alerts.")
render_footer()

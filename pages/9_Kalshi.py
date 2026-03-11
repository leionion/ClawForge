"""Kalshi — CFTC-regulated prediction markets (read-only)."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="Kalshi | ClawForge", page_icon="📋", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Kalshi", "CFTC-regulated prediction markets — Fed, GDP, CPI, BTC. Read-only monitoring.", "📋")

if not is_gateway_ready():
    st.info("Install Kalshi skill: `clawhub install kalshi-trader` then start OpenClaw gateway.")
    st.markdown("**No auth required** — uses Kalshi public API.")
    onboarding_gateway()
    render_footer()
    st.stop()

presets = [
    "Show Fed rate decision markets (KXFED)",
    "Latest BTC price range markets (KXBTC)",
    "US GDP forecast markets (KXGDP)",
    "Trending Kalshi markets",
]
choice = st.selectbox("Quick command", ["— Custom —"] + presets, key="kalshi_cmd")
if choice == "— Custom —":
    cmd = st.text_input("Your command", placeholder="e.g. Show CPI inflation markets", key="kalshi_input")
else:
    cmd = choice

if cmd and st.button("Execute", key="kalshi_run"):
    with st.spinner("Kalshi..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-kalshi")
    if ok:
        st.success("Done")
        st.markdown(out[:3000] if out else "—")
    else:
        st.error(out[:400])

st.caption("Trade execution requires separate Kalshi API integration. This skill is monitoring only.")
render_footer()

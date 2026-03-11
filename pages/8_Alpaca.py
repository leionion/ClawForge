"""Alpaca — US stocks, ETFs, options via OpenClaw."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="Alpaca | ClawForge", page_icon="📉", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Alpaca", "US stocks, ETFs, options. Paper & live trading. Zero commission for stocks.", "📉")

security_notice()

if not is_gateway_ready():
    st.info("Install: `clawhub install alpaca-trading` then start OpenClaw gateway.")
    st.markdown("""
    **API:** [alpaca.markets](https://alpaca.markets) — Paper (simulated) or live keys.
    """)
    onboarding_gateway()
    render_footer()
    st.stop()

presets = [
    "Buy 100 shares of AAPL",
    "Show my portfolio",
    "If NVDA drops more than 5%, sell half my position",
    "Check portfolio at market close, trim overweight positions",
]
choice = st.selectbox("Quick command", ["— Custom —"] + presets, key="alpaca_cmd")
if choice == "— Custom —":
    cmd = st.text_input("Your command", placeholder="e.g. Buy 50 shares of SPY", key="alpaca_input")
else:
    cmd = choice

if cmd and st.button("Execute", key="alpaca_run"):
    with st.spinner("Alpaca..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-alpaca")
    if ok:
        st.success("Done")
        st.markdown(out[:3000] if out else "—")
    else:
        st.error(out[:400])

st.caption("Start with paper trading. Conditional orders use polling — not native triggers.")
render_footer()

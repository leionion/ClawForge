"""Portfolio — Rebalancing, drift detection, cross-asset management."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="Portfolio | ClawForge", page_icon="📁", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Portfolio", "Cross-asset monitoring, drift detection, automated rebalancing.", "folder")

security_notice()

if not is_gateway_ready():
    st.info("Connect Alpaca (stocks) and/or BankrBot (crypto) skills for full portfolio view.")
    onboarding_gateway()
    render_footer()
    st.stop()

presets = [
    "Show my full portfolio — equities and crypto",
    "If ETH drops below $2,500, convert 20% to USDC",
    "Every Friday, rebalance if any position drifts >5% from target",
    "What's my current allocation vs target?",
]
choice = st.selectbox("Quick command", ["— Custom —"] + presets, key="port_cmd")
if choice == "— Custom —":
    cmd = st.text_input("Your command", placeholder="e.g. Trim overweight positions", key="port_input")
else:
    cmd = choice

if cmd and st.button("Execute", key="port_run"):
    with st.spinner("Checking portfolio..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-portfolio")
    if ok:
        st.success("Done")
        st.markdown(out[:3000] if out else "—")
    else:
        st.error(out[:400])

st.markdown("---")
st.info("**For real portfolio data:** Install `clawhub install alpaca-trading` and `clawhub install bankr`, then ensure the OpenClaw gateway is running. See Status page.")
render_footer()

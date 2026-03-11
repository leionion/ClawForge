"""Polyclaw — Polymarket prediction market trading via OpenClaw."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="Polyclaw | ClawForge", page_icon="📈", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Polyclaw", "Polymarket prediction markets — browse, trade, hedge discovery. CLOB trading.", "📈")

security_notice()

if not is_gateway_ready():
    st.info("Install: `clawhub install polyclaw` then start OpenClaw gateway.")
    st.markdown("""
    **Required env:**
    - `CHAINSTACK_NODE` — Polygon RPC
    - `POLYCLAW_PRIVATE_KEY` — EVM wallet (hex)
    - `OPENROUTER_API_KEY` — for hedge discovery
    """)
    onboarding_gateway()
    render_footer()
    st.stop()

presets = [
    "Browse trending Polymarket markets",
    "Show my positions on Polymarket",
    "What's the latest Fed rate market?",
    "Find arbitrage opportunities across markets",
]
choice = st.selectbox("Quick command", ["— Custom —"] + presets, key="polyclaw_cmd")
if choice == "— Custom —":
    cmd = st.text_input("Your command", placeholder="e.g. Show YES/NO markets for BTC above $80k", key="polyclaw_input")
else:
    cmd = choice

if cmd and st.button("Execute", key="polyclaw_run"):
    with st.spinner("Polyclaw..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-polyclaw")
    if ok:
        st.success("Done")
        st.markdown(out[:3000] if out else "—")
    else:
        st.error(out[:400])

st.markdown("---")
st.caption("One-time: `uv run python scripts/polyclaw.py wallet approve` — approve contracts on Polygon.")
render_footer()

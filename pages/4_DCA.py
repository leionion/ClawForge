"""DCA — Dollar Cost Averaging via OpenClaw crypto-trader."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="DCA | ClawForge", page_icon="📊", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("DCA — Dollar Cost Averaging", "Start DCA strategy via OpenClaw crypto-trader skill.", "📊")

security_notice()

if not is_gateway_ready():
    st.info("Install: `clawhub install crypto-trader` (or openclaw/skills crypto-trader)")
    onboarding_gateway()
    render_footer()
    st.stop()

symbol = st.selectbox("Symbol", ["BTC/USDT", "ETH/USDT", "SOL/USDT", "Other"])
if symbol == "Other":
    symbol = st.text_input("Symbol", "BTC/USDT")
amount = st.number_input("Amount per buy (USDT)", min_value=5, value=10)
interval = st.selectbox("Interval", ["daily", "weekly", "monthly"])

if st.button("Start DCA"):
    cmd = f"Start DCA strategy: buy {amount} USDT of {symbol} every {interval}. Use paper trading mode."
    with st.spinner("Starting DCA..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-dca")
    if ok:
        st.success("Sent to OpenClaw")
        st.markdown(out[:1500] if out else "Check OpenClaw for status.")
    else:
        st.error(out[:300])
render_footer()

"""Price Alerts — Set crypto price alerts via OpenClaw."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready

st.set_page_config(page_title="Price Alerts | ClawForge", page_icon="🔔", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Price Alerts", "Set price alerts for crypto. Telegram/Discord notifications.", "🔔")

security_notice()

if not is_gateway_ready():
    st.info("Install: `clawhub install price-tracker` or `clawhub install crypto-tracker`")
    onboarding_gateway()
    render_footer()
    st.stop()

symbol = st.selectbox("Symbol", ["BTC", "ETH", "SOL", "Other"])
if symbol == "Other":
    symbol = st.text_input("Symbol", "BTC")
price = st.number_input("Alert when price (USD)", min_value=0.0, value=90000.0, step=1000.0)
direction = st.radio("Alert when", ["drops below", "rises above"])

if st.button("Set Alert"):
    cmd = f"Set price alert for {symbol}: notify me when price {direction.replace(' ', 's ')} ${price:,.0f}"
    with st.spinner("Setting alert..."):
        ok, out, _ = chat_completion_with_fallback([{"role": "user", "content": cmd}], user="skillforge-alerts")
    if ok:
        st.success("Sent to OpenClaw")
        st.markdown(out[:1500] if out else "Check OpenClaw to confirm.")
    else:
        st.error(out[:300])
render_footer()

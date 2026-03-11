"""Chat with OpenClaw agent or Chutes LLM fallback."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.openclaw_gateway import chat_completion_with_fallback, is_gateway_ready
from config import has_llm, chat_via_llm_fallback, get_active_llm_name
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, render_sidebar_nav

st.set_page_config(page_title="Chat | ClawForge", page_icon="💬", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Chat with OpenClaw", "Talk to your OpenClaw agent. Full capabilities — tools, skills, memory.", "💬")

# Use OpenClaw when ready; otherwise use Chutes/LLM if configured
gateway_ready = is_gateway_ready()
use_llm_fallback = has_llm()
if "use_lightweight" not in st.session_state:
    st.session_state.use_lightweight = False
# When lightweight mode: bypass OpenClaw, use direct LLM (Groq/Ollama) — less CPU
use_openclaw = gateway_ready and not st.session_state.use_lightweight

if not use_openclaw and not use_llm_fallback:
    st.warning("**Chat needs an AI backend.** Free options:")
    st.markdown("""
    1. **Groq** (free tier): Add `GROQ_API_KEY` from [console.groq.com](https://console.groq.com)
    2. **Chutes**: Add `CHUTES_API_KEY` to .env
    3. **OpenClaw Gateway** — Full agent (tools, skills) with any provider above
    """)
    onboarding_gateway()
    render_footer()
    st.stop()

if use_openclaw:
    st.success("🦾 Connected to OpenClaw — full agent (tools, skills, memory)")
elif use_llm_fallback:
    st.info(f"💬 Using **{get_active_llm_name()}** — basic chat. Connect OpenClaw Gateway for full agent capabilities.")

# Option to use direct LLM (bypass OpenClaw) when gateway is running
if gateway_ready:
    with st.expander("⚡ Switch to direct LLM"):
        st.caption("Use Groq/Chutes directly (no OpenClaw tools). Helpful if the gateway has issues.")
        prev = st.session_state.use_lightweight
        st.session_state.use_lightweight = st.checkbox("Use lightweight chat (direct Groq)", value=prev, key="lightweight_chat")
        if st.session_state.use_lightweight:
            use_openclaw = False
            use_llm_fallback = True

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message OpenClaw..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if use_openclaw:
                # Try gateway first; on failure, auto-fallback to direct LLM with clear note
                ok, text, _ = chat_completion_with_fallback(
                    [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    agent_id="main",
                    user="skillforge-web",
                    use_fallback=has_llm(),
                )
                if not ok:
                    # No fallback available — keep error for st.error
                    pass
            else:
                ok, text = chat_via_llm_fallback(
                    [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
        if ok:
            st.markdown(text or "*No response*")
            st.session_state.messages.append({"role": "assistant", "content": text or ""})
        else:
            st.error(text)
            st.session_state.messages.pop()

if st.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()

if not use_openclaw:
    with st.expander("🦾 How to connect OpenClaw for full agent"):
        onboarding_gateway()

render_footer()

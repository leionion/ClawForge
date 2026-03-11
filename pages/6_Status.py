"""OpenClaw & Skill Forge status dashboard."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.openclaw_client import get_status, install_skill_to_workspace, skills_list
from core.openclaw_gateway import health_check, gateway_reachable, GATEWAY_URL, GATEWAY_TOKEN, chat_completion
from config import has_llm
from core.ui_components import inject_global_css, render_footer, onboarding_gateway, page_hero, security_notice, render_sidebar_nav

st.set_page_config(page_title="Status | ClawForge", page_icon="📊", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Status Dashboard", "System health and integration status", "📊")

security_notice()

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("#### 🦾 OpenClaw CLI")
    status = get_status()
    st.write("Installed:", "✅" if status["installed"] else "❌")
    st.write("Gateway port:", "✅" if status["gateway_running"] else "❌")
    st.write("Skill installed:", "✅" if status["skill_installed"] else "❌")
    st.caption(f"Workspace: {status['workspace']}")
    if not status["skill_installed"] and status["installed"]:
        if st.button("Install skill", key="install_skill"):
            ok, msg = install_skill_to_workspace()
            st.success(msg) if ok else st.error(msg)
            st.rerun()

with c2:
    st.markdown("#### 🌐 Gateway HTTP API")
    st.write("URL:", GATEWAY_URL)
    st.write("Token:", "✅ Set" if GATEWAY_TOKEN else "❌ Not set")
    st.write("Reachable:", "✅" if gateway_reachable() else "❌")
    ok, info = health_check()
    st.write("Authenticated:", "✅" if ok else "❌")
    if not ok and info.get("error"):
        st.caption(str(info["error"])[:120])
    if GATEWAY_TOKEN and gateway_reachable() and st.button("Test chat completions", key="test_chat"):
        chat_ok, chat_out = chat_completion([{"role": "user", "content": "Say OK"}], agent_id="main", user="status-test")
        st.success("Chat OK") if chat_ok else st.error(chat_out[:200] if chat_out else "No response")

with c3:
    st.markdown("#### 🤖 LLM (Chutes)")
    st.write("Chutes/Groq/OpenAI:", "✅" if has_llm() else "❌")
    st.caption("For decomposition & chat")

if not (GATEWAY_TOKEN and gateway_reachable()):
    onboarding_gateway()

st.divider()
st.markdown("#### OpenClaw Skills")
if status["installed"]:
    eligible = st.checkbox("Eligible only", False, key="eligible")
    if st.button("Refresh skills", key="refresh_skills"):
        st.rerun()
    ok, out = skills_list(eligible_only=eligible)
    if ok:
        st.code(out[:2000] + ("..." if len(out) > 2000 else ""), language="text")
    else:
        st.info(out or "Run openclaw gateway first")
else:
    st.info("Install OpenClaw to list skills")

with st.expander("Security rules for real money"):
    st.markdown("""
    1. **Verify every skill** — Check repo stars, commits, contributors
    2. **Use ClawSecure/ClawScan** — Scan skills before install
    3. **Isolate wallet** — Dedicated bot wallet only; never main
    4. **Run in container** — Docker, non-root, restricted network
    5. **Start with monitoring** — Let AI recommend; you decide
    6. **Audit permissions** — Revoke unused API keys; rotate monthly
    """)

st.divider()
with st.expander("🔧 Fix OpenClaw chat issues (rate limit, 404)"):
    st.markdown("""
If gateway fails, pages auto-use direct LLM (no intrusive message). To fix the gateway:
1. **Add model fallbacks** — Run: `python scripts/fix_openclaw_gateway.py` (adds Chutes fallback when Groq rate limits)
2. **Ensure API keys** — `GROQ_API_KEY` and `CHUTES_API_KEY` in `~/.openclaw/.env`
3. **Restart** — `pm2 restart openclaw-gateway`
""")
st.markdown("#### Resources")
st.markdown("""
- **[ClawHub](https://clawhub.ai)** — 13,700+ skills
- **[OpenClaw Docs](https://docs.openclaw.ai)** — Setup, channels, automation
- **Chat API:** Add `gateway.http.endpoints.chatCompletions.enabled: true` to `~/.openclaw/openclaw.json`
""")
render_footer()

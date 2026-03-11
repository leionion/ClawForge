"""Skill Forge — Decompose demands with Chutes LLM."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.ui_components import inject_global_css, render_footer, page_hero, render_sidebar_nav
from core.cutter import CutterEngine
from core.openclaw_client import is_openclaw_installed, invoke_agent

RUNNABLE = {
    "memory_backup": {"script": "skills/04-Process/memory_backup/memory_backup.py", "action": "backup"},
    "strategy_backtest": {"script": "skills/04-Process/strategy_backtest/strategy_backtest.py", "action": None},
}

st.set_page_config(page_title="Skill Forge | ClawForge", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
with st.sidebar:
    render_sidebar_nav()
page_hero("Skill Forge", "Decompose demands with Chutes LLM → run skills or send to OpenClaw", "⚡")

model = st.radio("Engine", ["keyword", "chutes"], format_func=lambda x: "Keyword" if x == "keyword" else "Chutes LLM", horizontal=True)
demand = st.text_input("What do you want?", placeholder="e.g. backup my chat memory, run backtest, take screenshot", label_visibility="collapsed")

if demand:
    with st.spinner("Decomposing..."):
        result = CutterEngine().process(demand, model=model)
    skills = [d["skill"] for d in result.get("decomposed", []) if d.get("skill") != "unknown"]
    if not skills:
        st.info("No match. Try different wording.")
    else:
        for s in skills:
            runnable = s in RUNNABLE
            st.write(f"**{s}** — {'🟢 Run' if runnable else '🔵 OpenClaw'}")
        first = next((s for s in skills if s in RUNNABLE), None)
        if first:
            if st.button("▶ Run " + first):
                import subprocess
                cfg = RUNNABLE[first]
                script = ROOT / cfg["script"]
                cmd = [sys.executable, str(script)] + ([cfg["action"]] if cfg.get("action") else [])
                r = subprocess.run(cmd, cwd=script.parent, capture_output=True, text=True, timeout=60)
                st.success(r.stdout[:500] if r.returncode == 0 else r.stderr[:300])
        elif is_openclaw_installed():
            if st.button("🦾 Run via OpenClaw"):
                ok, out = invoke_agent(demand)
                if ok:
                    st.success(out[:500])
                else:
                    st.error(out[:300])
    with st.expander("Details"):
        st.markdown(result.get("markdown", ""))
render_footer()

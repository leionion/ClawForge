#!/usr/bin/env python3
"""
metaskill — OpenClaw Skill Forge CLI
Describe what you want → Cutter finds skills → Run if possible.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RUNNABLE_SKILLS = {
    "memory_backup": {"path": "skills/04-Process/memory_backup/memory_backup.py", "action": "backup"},
    "strategy_backtest": {"path": "skills/04-Process/strategy_backtest/strategy_backtest.py", "action": None},
}


def run_cutter(demand: str, model: str = None) -> dict:
    from core.cutter import CutterEngine
    return CutterEngine().process(demand, model=model)


def run_skill(name: str) -> bool:
    if name not in RUNNABLE_SKILLS:
        return False
    cfg = RUNNABLE_SKILLS[name]
    script = ROOT / cfg["path"]
    if not script.exists():
        return False
    cmd = [sys.executable, str(script)]
    if cfg.get("action"):
        cmd.append(cfg["action"])
    try:
        subprocess.run(cmd, cwd=script.parent, check=True)
        return True
    except Exception:
        return False


def main():
    p = argparse.ArgumentParser(description="OpenClaw Skill Forge — Describe what you want, get it done.")
    p.add_argument("demand", nargs="*")
    p.add_argument("--list", action="store_true", help="List all skills")
    p.add_argument("--decompose-only", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("--model", choices=["gpt", "chutes", "keyword"], default="keyword",
                   help="Use LLM (gpt/chutes) for decomposition (needs CHUTES_API_KEY or OPENAI_API_KEY)")
    args = p.parse_args()

    if args.list:
        skills_dir = ROOT / "skills"
        for cat in sorted(skills_dir.iterdir()) if skills_dir.exists() else []:
            if cat.is_dir():
                for sd in cat.iterdir():
                    if sd.is_dir() and (sd / "_meta.json").exists():
                        runnable = " ✓" if sd.name in RUNNABLE_SKILLS else ""
                        print(f"  {sd.name} ({cat.name}){runnable}")
        return 0

    demand = " ".join(args.demand).strip()
    if not demand:
        p.print_help()
        return 1

    result = run_cutter(demand, model=args.model)
    skills = [d["skill"] for d in result.get("decomposed", []) if d.get("skill") != "unknown"]

    if args.json:
        print(json.dumps({"demand": demand, "skills": skills, "result": result}, indent=2))
        return 0

    print(result.get("markdown", ""))
    if args.decompose_only:
        return 0

    for sn in skills:
        if sn in RUNNABLE_SKILLS:
            print(f"\n▶ Running {sn}...")
            ok = run_skill(sn)
            print(f"✅ {sn} completed." if ok else f"⚠ {sn} failed.")
            return 0 if ok else 1

    if skills:
        openclaw_skills = [s for s in skills if s not in RUNNABLE_SKILLS]
        if openclaw_skills:
            try:
                from core.openclaw_client import is_openclaw_installed, invoke_agent
                if is_openclaw_installed():
                    print(f"\n🦾 Sending to OpenClaw: {demand}")
                    ok, out = invoke_agent(demand)
                    print(out[:500] if out else ("✅ Sent" if ok else "⚠ Failed"))
                    return 0 if ok else 1
            except Exception:
                pass
        print(f"\n💡 Matched: {', '.join(skills)}. Install OpenClaw to execute.")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)

#!/usr/bin/env python3
"""
Fix OpenClaw gateway — add model fallbacks (Groq + Chutes) so rate limits
don't cause full failure. Run: python scripts/fix_openclaw_gateway.py
"""
import json
import os
from pathlib import Path

CFG = Path.home() / ".openclaw" / "openclaw.json"

def main():
    if not CFG.exists():
        print(f"Config not found: {CFG}")
        return 1
    with open(CFG) as f:
        c = json.load(f)

    agents = c.setdefault("agents", {})
    defaults = agents.setdefault("defaults", {})
    model = defaults.get("model")

    # Ensure model has fallbacks for rate-limit resilience
    changed = False
    if isinstance(model, str):
        providers = c.get("models", {}).get("providers", {})
        fallbacks = []
        if "chutes" in providers:
            fallbacks.append("chutes/meta-llama/Llama-3.1-8B-Instruct")
        if "groq" not in str(model).lower() and "groq" in providers:
            fallbacks.append("groq/llama-3.1-8b-instant")
        defaults["model"] = {"primary": model, "fallbacks": fallbacks}
        print(f"Added fallbacks: {fallbacks}")
        changed = True
    elif isinstance(model, dict) and not model.get("fallbacks"):
        providers = c.get("models", {}).get("providers", {})
        fallbacks = []
        if "chutes" in providers:
            fallbacks.append("chutes/meta-llama/Llama-3.1-8B-Instruct")
        defaults["model"]["fallbacks"] = fallbacks
        print(f"Added fallbacks: {fallbacks}")
        changed = True
    if changed:
        with open(CFG, "w") as f:
            json.dump(c, f, indent=2)
        print(f"Updated {CFG}. Restart: pm2 restart openclaw-gateway")
    else:
        print("Config already has fallbacks.")
    return 0

if __name__ == "__main__":
    exit(main())

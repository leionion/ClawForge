"""
OpenClaw Skill Forge — OpenClaw Integration
Check OpenClaw, install our skill, invoke agent.
"""
import json
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPENCLAW_WORKSPACE = Path.home() / ".openclaw" / "workspace"
OPENCLAW_SKILLS_DIR = OPENCLAW_WORKSPACE / "skills"
OUR_SKILL_SRC = ROOT / "openclaw-skill"
OUR_SKILL_NAME = "metaskillbase"


def is_openclaw_installed() -> bool:
    """Check if OpenClaw CLI is available."""
    try:
        r = subprocess.run(
            ["openclaw", "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        return r.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def is_gateway_running(port: int = 18789) -> bool:
    """Check if OpenClaw Gateway is running."""
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex(("127.0.0.1", port))
        s.close()
        return result == 0
    except Exception:
        return False


def install_skill_to_workspace() -> tuple[bool, str]:
    """
    Copy our openclaw-skill into OpenClaw workspace.
    Returns (success, message).
    """
    if not OUR_SKILL_SRC.exists():
        return False, f"Skill source not found: {OUR_SKILL_SRC}"
    dest = OPENCLAW_SKILLS_DIR / OUR_SKILL_NAME
    try:
        OPENCLAW_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(OUR_SKILL_SRC, dest)
        return True, f"Skill installed to {dest}"
    except Exception as e:
        return False, str(e)


def is_skill_installed() -> bool:
    """Check if our skill is installed in OpenClaw workspace."""
    return (OPENCLAW_SKILLS_DIR / OUR_SKILL_NAME).exists()


def invoke_agent(message: str, timeout: int = 60) -> tuple[bool, str]:
    """
    Invoke OpenClaw agent with a message.
    Returns (success, output).
    """
    if not is_openclaw_installed():
        return False, "OpenClaw CLI not installed. Run: npm install -g openclaw"
    try:
        r = subprocess.run(
            ["openclaw", "agent", "--agent", "main", "--message", message, "--json"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        out = r.stdout or r.stderr or ""
        if r.returncode != 0:
            return False, out
        # Parse JSON and extract reply text for cleaner display
        try:
            data = json.loads(out)
            payloads = (data.get("result") or {}).get("payloads") or []
            if payloads and isinstance(payloads[0], dict) and payloads[0].get("text"):
                return True, payloads[0]["text"]
        except (json.JSONDecodeError, (IndexError, KeyError, TypeError)):
            pass
        return True, out
    except subprocess.TimeoutExpired:
        return False, "OpenClaw agent timed out"
    except Exception as e:
        return False, str(e)


def get_status() -> dict:
    """Get OpenClaw integration status."""
    return {
        "installed": is_openclaw_installed(),
        "gateway_running": is_gateway_running(),
        "skill_installed": is_skill_installed(),
        "workspace": str(OPENCLAW_WORKSPACE),
    }


def skills_list(eligible_only: bool = False) -> tuple[bool, str]:
    """List OpenClaw skills via CLI. Returns (success, output)."""
    if not is_openclaw_installed():
        return False, "OpenClaw CLI not installed"
    try:
        cmd = ["openclaw", "skills", "list", "--eligible"] if eligible_only else ["openclaw", "skills", "list"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return r.returncode == 0, r.stdout or r.stderr or ""
    except Exception as e:
        return False, str(e)

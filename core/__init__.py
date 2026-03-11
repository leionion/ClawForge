# OpenClaw Skill Forge — Cutter Engine
__version__ = "1.0.0"
from .cutter import Cutter
from .openclaw_client import (
    is_openclaw_installed,
    is_gateway_running,
    is_skill_installed,
    install_skill_to_workspace,
    invoke_agent,
    get_status,
)

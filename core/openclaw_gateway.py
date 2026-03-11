"""
OpenClaw Skill Forge — Gateway HTTP API
Chat completions (OpenAI-compatible) and tools invoke.
"""
import json
import os
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

GATEWAY_URL = os.environ.get("OPENCLAW_GATEWAY_URL", "http://127.0.0.1:18789").rstrip("/")
GATEWAY_TOKEN = os.environ.get("OPENCLAW_GATEWAY_TOKEN", "") or os.environ.get("OPENCLAW_GATEWAY_PASSWORD", "")

# For backwards-compat import
OPENCLAW_GATEWAY_TOKEN = GATEWAY_TOKEN


def _request(method: str, path: str, data: dict = None, timeout: int = 120) -> tuple[int, dict]:
    """Make HTTP request to Gateway. Returns (status_code, response_dict)."""
    url = f"{GATEWAY_URL}{path}"
    headers = {"Content-Type": "application/json"}
    if GATEWAY_TOKEN:
        headers["Authorization"] = f"Bearer {GATEWAY_TOKEN}"
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out = json.loads(r.read().decode()) if r.length else {}
            return r.status, out
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode() if e.fp else "{}"
            return e.code, json.loads(body) if body.strip() else {}
        except Exception:
            return e.code, {"error": str(e)}
    except Exception as e:
        return 0, {"error": str(e)}


# Patterns that indicate the gateway/LLM returned an error as content (e.g. Chutes 404)
_ERROR_CONTENT_PATTERNS = (
    "404", "429", "500", "status code", "no body", "rate limit", "too many requests",
    "openclaw gateway had an issue", "using direct llm",  # gateway fallback — trigger our fallback
)


def _is_error_content(content: str) -> bool:
    """True if content looks like an HTTP/API error message."""
    if not content or len(content) < 5:
        return True
    lower = content.lower().strip()
    return any(p in lower for p in _ERROR_CONTENT_PATTERNS)


def chat_completion(messages: list, agent_id: str = "main", stream: bool = False, user: str = None) -> tuple[bool, str]:
    """
    Send chat to OpenClaw via /v1/chat/completions.
    Returns (success, response_text_or_error).
    """
    if not GATEWAY_TOKEN:
        return False, "Set OPENCLAW_GATEWAY_TOKEN in .env"
    payload = {
        "model": f"openclaw:{agent_id}",
        "messages": messages,
        "stream": stream,
    }
    if user:
        payload["user"] = user
    status, resp = _request("POST", "/v1/chat/completions", payload, timeout=90)
    if status != 200:
        err_obj = resp.get("error")
        if isinstance(err_obj, dict):
            err = err_obj.get("message", err_obj.get("error", str(resp)))
        else:
            err = str(err_obj) if err_obj is not None else str(resp)
        return False, err or f"Gateway returned {status}"
    try:
        choices = resp.get("choices") or []
        if not choices:
            return False, "No choices in response"
        msg = choices[0].get("message") if isinstance(choices[0], dict) else {}
        content = msg.get("content", "") if isinstance(msg, dict) else str(msg)
        content = (content or "").strip()
        # Gateway returned 200 but content is an error (e.g. Chutes 404, rate limit)
        if _is_error_content(content):
            hint = "Add GROQ_API_KEY to .env and ~/.openclaw/.env, set model to groq/llama-3.1-8b-instant in ~/.openclaw/openclaw.json, restart gateway. Or use 'Switch to direct LLM' below."
            if content and "rate limit" in content.lower():
                hint = "Rate limit hit. Wait a few minutes, or add GROQ_API_KEY to ~/.openclaw/.env and set model to groq/llama-3.1-8b-instant. Or use 'Switch to direct LLM' for Groq."
            return False, f"OpenClaw gateway: {content[:200]}. Fix: {hint}"
        return True, content or ""
    except (IndexError, KeyError, TypeError) as e:
        return False, str(resp) if resp else str(e)


def chat_completion_with_fallback(
    messages: list, agent_id: str = "main", user: str = None, use_fallback: bool = True
) -> tuple[bool, str, dict]:
    """
    Try OpenClaw gateway first. On failure, fall back to direct LLM (Chutes/Groq/OpenAI).
    Returns (success, response_text, meta). Meta has "used_fallback": True when direct LLM was used.
    Response is clean—no prepended note.
    """
    ok, out = chat_completion(messages, agent_id=agent_id, user=user)
    if ok:
        return True, out, {}
    if use_fallback:
        try:
            from config import chat_via_llm_fallback, has_llm
            if has_llm():
                ok2, out2 = chat_via_llm_fallback(messages)
                if ok2:
                    return True, out2, {"used_fallback": True}
        except Exception:
            pass
    return False, out, {}


def tool_invoke(tool: str, args: dict = None, action: str = "json") -> tuple[bool, any]:
    """
    Invoke a Gateway tool via /tools/invoke.
    Returns (success, result).
    """
    if not GATEWAY_TOKEN:
        return False, "Set OPENCLAW_GATEWAY_TOKEN in .env"
    payload = {"tool": tool, "action": action, "args": args or {}}
    status, resp = _request("POST", "/tools/invoke", payload)
    if status != 200:
        return False, resp.get("error", resp)
    return True, resp.get("result", resp)


def sessions_list(limit: int = 20, kinds: str = None) -> tuple[bool, list]:
    """List OpenClaw sessions."""
    args = {"limit": limit}
    if kinds:
        args["kinds"] = kinds
    ok, res = tool_invoke("sessions_list", args)
    if not ok:
        return False, []
    return True, res if isinstance(res, list) else [res]


def sessions_history(session_key: str, limit: int = 50) -> tuple[bool, list]:
    """Get session history."""
    ok, res = tool_invoke("sessions_history", {"sessionKey": session_key, "limit": limit})
    if not ok:
        return False, []
    return True, res if isinstance(res, list) else [res]


def gateway_reachable() -> bool:
    """Check if Gateway port is open (no auth)."""
    try:
        import socket
        from urllib.parse import urlparse
        u = urlparse(GATEWAY_URL)
        host = u.hostname or "127.0.0.1"
        port = u.port or 18789
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        r = s.connect_ex((host, port))
        s.close()
        return r == 0
    except Exception:
        return False


def health_check() -> tuple[bool, dict]:
    """Check Gateway health. Try sessions_list (requires auth)."""
    if not GATEWAY_TOKEN:
        return False, {"error": "Set OPENCLAW_GATEWAY_TOKEN in .env"}
    if not gateway_reachable():
        return False, {"error": "Gateway not reachable. Run: openclaw gateway"}
    ok, res = tool_invoke("sessions_list", {"limit": 1})
    return ok, ({"sessions": res} if ok else {"error": res})


def is_gateway_ready() -> bool:
    """Check if Gateway is reachable and auth works."""
    ok, _ = health_check()
    return ok

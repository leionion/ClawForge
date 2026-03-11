"""
OpenClaw Skill Forge — Configuration
Chutes API (cloud) — no local LLM inference. Add CHUTES_API_KEY.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

# === FREE OPTIONS (no or free API key) ===
# Ollama: 100% free, local — curl -fsSL https://ollama.com/install.sh | sh && ollama pull llama3.2
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")

# Groq: Free tier — https://console.groq.com (no card required)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant")

# Chutes (may have free tier)
CHUTES_API_KEY = os.environ.get("CHUTES_API_KEY", "")
CHUTES_BASE_URL = os.environ.get("CHUTES_BASE_URL", "https://api.chutes.ai").rstrip("/")
if CHUTES_BASE_URL and "/v1" not in CHUTES_BASE_URL:
    CHUTES_BASE_URL = f"{CHUTES_BASE_URL}/v1"
CHUTES_MODEL = os.environ.get("CHUTES_MODEL", "meta-llama/Llama-3.1-8B-Instruct")

# LLM Provider: chutes | groq | ollama | openai (default: chutes — API only, no local inference)
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "chutes").lower()

# Paid fallbacks
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# OpenClaw Gateway
OPENCLAW_GATEWAY_URL = os.environ.get("OPENCLAW_GATEWAY_URL", "http://127.0.0.1:18789").rstrip("/")
OPENCLAW_GATEWAY_TOKEN = os.environ.get("OPENCLAW_GATEWAY_TOKEN", "") or os.environ.get("OPENCLAW_GATEWAY_PASSWORD", "")


def _ollama_chat(messages: list, model: str = None) -> tuple[bool, str]:
    """Chat via Ollama (free, local). No API key. Returns (success, text)."""
    import json
    try:
        import urllib.request
        url = f"{OLLAMA_BASE_URL}/v1/chat/completions"
        data = json.dumps({
            "model": model or OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
        }).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=120) as r:
            out = json.loads(r.read().decode())
            text = out.get("choices", [{}])[0].get("message", {}).get("content") or ""
            return True, text
    except Exception as e:
        return False, str(e)


def _ollama_available() -> bool:
    """Check if Ollama is reachable."""
    try:
        import urllib.request
        req = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=2) as _:
            return True
    except Exception:
        return False


def _groq_chat(messages: list, model: str = None) -> tuple[bool, str]:
    """Chat via Groq (free tier). Returns (success, text)."""
    if not GROQ_API_KEY:
        return False, "Set GROQ_API_KEY in .env (free at console.groq.com)"
    try:
        from openai import OpenAI
        client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")
        r = client.chat.completions.create(
            model=model or GROQ_MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=2048,
        )
        return True, (r.choices[0].message.content or "")
    except Exception as e:
        return False, str(e)


def _chutes_completion(prompt: str, model: str = None) -> str:
    """Direct Chutes API call. Returns response text or ''."""
    import json
    try:
        import urllib.request
        url = f"{CHUTES_BASE_URL.rstrip('/')}/chat/completions"
        data = json.dumps({
            "model": model or CHUTES_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 1024,
        }).encode("utf-8")
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json", "X-API-Key": CHUTES_API_KEY},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            out = json.loads(r.read().decode())
            return (out.get("choices", [{}])[0].get("message", {}).get("content") or "")
    except Exception:
        return ""


def _chutes_chat(messages: list, model: str = None) -> tuple[bool, str]:
    """Chat via Chutes. Returns (success, text)."""
    import json
    try:
        import urllib.request
        url = f"{CHUTES_BASE_URL.rstrip('/')}/chat/completions"
        data = json.dumps({
            "model": model or CHUTES_MODEL,
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 2048,
        }).encode("utf-8")
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json", "X-API-Key": CHUTES_API_KEY},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=90) as r:
            out = json.loads(r.read().decode())
            return True, (out.get("choices", [{}])[0].get("message", {}).get("content") or "")
    except Exception as e:
        return False, str(e)


def chat_via_llm_fallback(messages: list) -> tuple[bool, str]:
    """Chat: Groq → Chutes → OpenAI. No local inference. Groq first (most reliable)."""
    # 1. Groq — free tier, cloud, most reliable
    if GROQ_API_KEY:
        ok, text = _groq_chat(messages)
        if ok:
            return True, text
    # 2. Chutes — cloud API
    if CHUTES_API_KEY and CHUTES_BASE_URL:
        ok, text = _chutes_chat(messages)
        if ok:
            return True, text
    if OPENAI_API_KEY:
        try:
            from openai import OpenAI
            r = OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
                model="gpt-4o-mini", messages=messages, temperature=0.3, max_tokens=2048,
            )
            return True, (r.choices[0].message.content or "")
        except Exception as e:
            return False, str(e)
    return False, "Set CHUTES_API_KEY in .env for Chutes LLM (no local inference)"


def get_llm_client():
    """Return (client, model) for Skill Forge. Uses Chutes API — no local inference."""
    if LLM_PROVIDER == "chutes" and CHUTES_API_KEY:
        class ChutesClient:
            class _Completions:
                def create(inner_self, model, messages, **kw):
                    prompt = next((m.get("content") for m in reversed(messages) if m.get("content")), "")
                    text = _chutes_completion(prompt, model)
                    msg = type("Msg", (), {"content": text})()
                    return type("Resp", (), {"choices": [type("C", (), {"message": msg})()]})()
            chat = _Completions()
        return ChutesClient(), CHUTES_MODEL
    if LLM_PROVIDER == "ollama" and _ollama_available():
        class OllamaClient:
            class _Completions:
                def create(inner_self, model, messages, **kw):
                    ok, text = _ollama_chat(messages, model or OLLAMA_MODEL)
                    msg = type("Msg", (), {"content": text})()
                    return type("Resp", (), {"choices": [type("C", (), {"message": msg})()]})()
            chat = _Completions()
        return OllamaClient(), OLLAMA_MODEL
    if LLM_PROVIDER == "groq" and GROQ_API_KEY:
        try:
            from openai import OpenAI
            return OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1"), GROQ_MODEL
        except Exception:
            pass
    if OPENAI_API_KEY:
        try:
            from openai import OpenAI
            return OpenAI(api_key=OPENAI_API_KEY), "gpt-4o-mini"
        except Exception:
            pass
    return None, None


def has_llm() -> bool:
    """True if any LLM API is configured (Groq, Chutes, OpenAI)."""
    return bool(GROQ_API_KEY or (CHUTES_API_KEY and CHUTES_BASE_URL) or OPENAI_API_KEY)


def get_active_llm_name() -> str:
    """Return human-readable name of the active LLM for UI."""
    if GROQ_API_KEY:
        return "Groq API"
    if CHUTES_API_KEY:
        return "Chutes API"
    if OPENAI_API_KEY:
        return "OpenAI"
    return "None"

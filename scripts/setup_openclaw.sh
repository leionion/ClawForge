#!/bin/bash
# OpenClaw Skill Forge — Install OpenClaw, configure gateway, and our skill
set -e
cd "$(dirname "$0")/.."

echo "=== OpenClaw Skill Forge — OpenClaw Setup ==="

# Check Node.js (OpenClaw requires v22+)
NODE_VER=$(node -v 2>/dev/null | sed 's/v//' | cut -d. -f1)
if [ -z "$NODE_VER" ] || [ "$NODE_VER" -lt 22 ]; then
  echo "Node.js 22+ required. Current: $(node -v 2>/dev/null || echo 'not found')"
  echo "Install: curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt-get install -y nodejs"
  exit 1
fi

# Install OpenClaw CLI
if ! command -v openclaw >/dev/null 2>&1; then
  echo "Installing OpenClaw CLI..."
  npm install -g openclaw 2>/dev/null || pnpm add -g openclaw 2>/dev/null || {
    echo "Run manually: npm install -g openclaw"
    exit 1
  }
fi

echo "OpenClaw CLI: $(openclaw --version 2>/dev/null || echo 'installed')"

# Run OpenClaw setup to create config
if [ ! -f "$HOME/.openclaw/openclaw.json" ]; then
  echo "Running openclaw setup..."
  openclaw setup || true
fi

# Ensure gateway config: mode, HTTP chat completions, auth
CONFIG="$HOME/.openclaw/openclaw.json"
if ! grep -q "chatCompletions" "$CONFIG" 2>/dev/null; then
  echo "Configuring gateway HTTP chat completions..."
  python3 << 'PYEOF'
import json, os
cfg = os.path.expanduser("~/.openclaw/openclaw.json")
with open(cfg) as f:
  c = json.load(f)
c.setdefault("gateway", {})
c["gateway"]["mode"] = "local"
c["gateway"]["http"] = {"endpoints": {"chatCompletions": {"enabled": True}}}
if "auth" not in c["gateway"]:
  c["gateway"]["auth"] = {"mode": "token", "token": "${OPENCLAW_GATEWAY_TOKEN}"}
with open(cfg, "w") as f:
  json.dump(c, f, indent=2)
PYEOF
fi

# Add Ollama (free) as primary provider
if ! grep -q '"ollama"' "$CONFIG" 2>/dev/null; then
  echo "Adding Ollama (free, local) as primary model..."
  python3 << 'PYEOF'
import json, os
cfg = os.path.expanduser("~/.openclaw/openclaw.json")
with open(cfg) as f:
  c = json.load(f)
c.setdefault("models", {})["providers"] = c.get("models", {}).get("providers", {})
c["models"]["providers"]["ollama"] = {
  "baseUrl": "http://localhost:11434/v1",
  "api": "openai-completions",
  "models": [{"id": "llama3.2", "name": "Llama 3.2 (free)", "contextWindow": 128000}]
}
c.setdefault("agents", {})["defaults"] = c.get("agents", {}).get("defaults", {})
c["agents"]["defaults"]["model"] = {"primary": "ollama/llama3.2", "fallbacks": []}
c["agents"]["defaults"]["workspace"] = os.path.expanduser("~/.openclaw/workspace")
with open(cfg, "w") as f:
  json.dump(c, f, indent=2)
PYEOF
fi

# Add Chutes as fallback if we have the key
[ -f .env ] && export $(grep -v '^#' .env | xargs) 2>/dev/null
if [ -n "$CHUTES_API_KEY" ] && ! grep -q "chutes" "$CONFIG" 2>/dev/null; then
  echo "Adding Chutes as fallback provider..."
  python3 << 'PYEOF'
import json, os
cfg = os.path.expanduser("~/.openclaw/openclaw.json")
with open(cfg) as f:
  c = json.load(f)
c.setdefault("models", {})["providers"] = c.get("models", {}).get("providers", {})
c["models"]["providers"]["chutes"] = {
  "baseUrl": "https://api.chutes.ai/v1",
  "api": "openai-completions",
  "headers": {"X-API-Key": "${CHUTES_API_KEY}"},
  "models": [{"id": "meta-llama/Llama-3.1-8B-Instruct", "name": "Llama 3.1 8B", "contextWindow": 131072}]
}
m = c.get("agents", {}).get("defaults", {}).get("model", "ollama/llama3.2")
c.setdefault("agents", {})["defaults"] = c.get("agents", {}).get("defaults", {})
if isinstance(m, dict):
  c["agents"]["defaults"]["model"] = m
  c["agents"]["defaults"]["model"].setdefault("fallbacks", []).append("chutes/meta-llama/Llama-3.1-8B-Instruct")
else:
  c["agents"]["defaults"]["model"] = {"primary": m, "fallbacks": ["chutes/meta-llama/Llama-3.1-8B-Instruct"]}
with open(cfg, "w") as f:
  json.dump(c, f, indent=2)
PYEOF
fi

# Generate and set gateway token if missing
if ! grep -q OPENCLAW_GATEWAY_TOKEN .env 2>/dev/null; then
  TOKEN=$(openssl rand -hex 32)
  echo "" >> .env
  echo "# OpenClaw Gateway" >> .env
  echo "OPENCLAW_GATEWAY_TOKEN=$TOKEN" >> .env
  echo "OPENCLAW_GATEWAY_URL=http://127.0.0.1:18789" >> .env
  echo "OPENCLAW_GATEWAY_TOKEN=$TOKEN" >> "$HOME/.openclaw/.env" 2>/dev/null || echo "OPENCLAW_GATEWAY_TOKEN=$TOKEN" > "$HOME/.openclaw/.env"
  echo "Generated OPENCLAW_GATEWAY_TOKEN in .env and ~/.openclaw/.env"
fi

# Copy LLM keys to OpenClaw env so gateway can use them
[ -f .env ] && source .env 2>/dev/null || true
if [ -n "${GROQ_API_KEY}" ] && ! grep -q GROQ_API_KEY "$HOME/.openclaw/.env" 2>/dev/null; then
  echo "GROQ_API_KEY=$GROQ_API_KEY" >> "$HOME/.openclaw/.env"
  echo "Added GROQ_API_KEY to ~/.openclaw/.env (recommended for reliable inference)"
fi
if [ -n "$CHUTES_API_KEY" ] && ! grep -q CHUTES_API_KEY "$HOME/.openclaw/.env" 2>/dev/null; then
  echo "CHUTES_API_KEY=$CHUTES_API_KEY" >> "$HOME/.openclaw/.env"
fi

# Create workspace and install skill
WORKSPACE="$HOME/.openclaw/workspace"
SKILLS="$WORKSPACE/skills"
mkdir -p "$SKILLS"
SKILL_SRC="$(pwd)/openclaw-skill"
SKILL_DEST="$SKILLS/metaskillbase"
if [ -d "$SKILL_SRC" ]; then
  rm -rf "$SKILL_DEST"
  cp -r "$SKILL_SRC" "$SKILL_DEST"
  echo "Skill installed to $SKILL_DEST"
fi

echo ""
echo "Done. Start the gateway:"
echo "  ./scripts/start_openclaw_gateway.sh"
echo "  # or: openclaw gateway --port 18789"
echo ""
echo "Then run the web app: streamlit run web_app.py"

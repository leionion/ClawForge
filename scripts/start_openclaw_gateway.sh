#!/bin/bash
# Start OpenClaw Gateway for Skill Forge (Chat, BankrBot, DCA, Price Alerts)
set -e
cd "$(dirname "$0")/.."

# Load project .env
[ -f .env ] && export $(grep -v '^#' .env | xargs)

# Ensure OpenClaw .env has required vars (for gateway process)
OPENCLAW_ENV="$HOME/.openclaw/.env"
[ -f "$OPENCLAW_ENV" ] || touch "$OPENCLAW_ENV"
if ! grep -q OPENCLAW_GATEWAY_TOKEN "$OPENCLAW_ENV" 2>/dev/null; then
  echo "OPENCLAW_GATEWAY_TOKEN not in ~/.openclaw/.env. Run: ./scripts/setup_openclaw.sh"
  exit 1
fi
if ! grep -q CHUTES_API_KEY "$OPENCLAW_ENV" 2>/dev/null && [ -n "$CHUTES_API_KEY" ]; then
  echo "CHUTES_API_KEY=$CHUTES_API_KEY" >> "$OPENCLAW_ENV"
fi

# Start gateway
echo "Starting OpenClaw Gateway on port 18789..."
cd "$HOME/.openclaw"
exec openclaw gateway --port 18789

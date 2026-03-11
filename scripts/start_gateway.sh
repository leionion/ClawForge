#!/bin/bash
# Start OpenClaw gateway with env loaded — ensures API keys reach the process
set -e
cd /root/.openclaw
[ -f .env ] && set -a && source .env && set +a
exec openclaw gateway --port 18789

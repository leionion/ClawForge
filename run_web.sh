#!/bin/bash
# OpenClaw Skill Forge — Start Web App (port 8503)
cd "$(dirname "$0")"
echo "OpenClaw Skill Forge — starting on port 8503..."
# Kill any existing process on 8503
if command -v lsof >/dev/null 2>&1; then
  pid=$(lsof -ti :8503 2>/dev/null)
  if [ -n "$pid" ]; then
    echo "Stopping existing process on 8503 (PID $pid)..."
    kill -9 $pid 2>/dev/null || true
    sleep 1
  fi
fi
streamlit run web_app.py --server.port 8503

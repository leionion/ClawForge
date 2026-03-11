#!/bin/bash
# Install Ollama — 100% free local LLM (no API key, no cost)
set -e

echo "=== Installing Ollama (free, local LLM) ==="

if command -v ollama >/dev/null 2>&1; then
  echo "Ollama already installed: $(ollama --version 2>/dev/null || echo 'ok')"
else
  echo "Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
fi

echo ""
echo "Pulling default model (llama3.2, ~2GB)..."
ollama pull llama3.2 2>/dev/null || ollama pull llama3.2

echo ""
echo "✅ Ollama ready. Start server: ollama serve (often auto-started)"
echo "   Chat will use Ollama automatically — no API key needed."

/**
 * PM2 Ecosystem — ClawForge
 * Run: pm2 start ecosystem.config.cjs
 * Save: pm2 save && pm2 startup
 */
const fs = require("fs");
const path = require("path");
let CHUTES = "", GROQ = "", TOKEN = "";
try {
  const openclawEnv = path.join(process.env.HOME || "/root", ".openclaw", ".env");
  const forgeEnv = path.join(process.env.HOME || "/root", "ClawForge", ".env");
  for (const envPath of [openclawEnv, forgeEnv]) {
    try {
      const raw = fs.readFileSync(envPath, "utf8");
      if (!CHUTES) { const m = raw.match(/CHUTES_API_KEY=([^\s#]+)/); if (m) CHUTES = m[1].trim().replace(/^["']|["']$/g, ""); }
      if (!GROQ) { const m = raw.match(/GROQ_API_KEY=([^\s#]+)/); if (m) GROQ = m[1].trim().replace(/^["']|["']$/g, ""); }
      if (!TOKEN) { const m = raw.match(/OPENCLAW_GATEWAY_TOKEN=([^\s#]+)/); if (m) TOKEN = m[1].trim().replace(/^["']|["']$/g, ""); }
    } catch (_) {}
  }
} catch (_) {}

module.exports = {
  apps: [
    {
      name: "skillforge",
      script: "/usr/local/bin/streamlit",
      args: "run web_app.py --server.port 8503 --server.headless true --server.address 0.0.0.0",
      cwd: "/root/ClawForge",
      interpreter: "none",
      autorestart: true,
      max_restarts: 10,
      min_uptime: "10s",
      env: { PORT: "8503" },
    },
    {
      name: "openclaw-gateway",
      script: "/root/ClawForge/scripts/start_gateway.sh",
      interpreter: "bash",
      cwd: "/root/.openclaw",
      autorestart: true,
      max_restarts: 10,
      min_uptime: "5s",
    },
  ],
};

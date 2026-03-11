"""
OpenClaw Skill Forge - Cutter Engine
Demand decomposition and skill extraction.
Supports: keyword (default), Chutes/OpenAI LLM (--model chutes/gpt).
"""

import json
import os
import re
from pathlib import Path


class Decomposer:
    """Demand decomposition engine"""
    
    def __init__(self, skill_index_path="Skill-Index.md"):
        self.skill_index_path = skill_index_path
        self.skill_registry = {}
    
    def load_skill_index(self, content):
        """Load skill index from markdown content"""
        # Parse skill entries from index
        pattern = r'## \[([^\]]+)\]\([^)]+\)\s*\n\s*([^\n#]+)'
        matches = re.findall(pattern, content)
        for name, desc in matches:
            self.skill_registry[name.strip().lower()] = {
                "name": name.strip(),
                "description": desc.strip()
            }
    
    def decompose(self, demand):
        """
        Decompose human demand into executable skills
        
        Args:
            demand: Human-readable demand string
            
        Returns:
            List of decomposed skill demands
        """
        demand_lower = demand.lower()
        decomposed = []
        
        # Keyword-based skill matching
        skill_keywords = {
            "open": ["open_app", "activate"],
            "close": ["close_app", "empty_trash"],
            "file": ["file_copy", "file_move", "file_delete", "mkdir"],
            "copy": ["file_copy"],
            "move": ["file_move"],
            "delete": ["file_delete"],
            "make directory": ["mkdir"],
            "screenshot": ["screenshot"],
            "brightness": ["brightness"],
            "volume": ["volume"],
            "ip": ["ip"],
            "eject": ["eject"],
            "spotlight": ["spotlight"],
            "calculator": ["calculator"],
            "calendar": ["calendar"],
            "clipboard": ["clipboard"],
            "dark mode": ["dark_mode"],
            "dictionary": ["dictionary"],
            "finder": ["finder"],
            "mail": ["mail"],
            "music": ["music"],
            "notify": ["notify"],
            "preferences": ["preferences"],
            "print": ["print"],
            "restart": ["restart"],
            "shutdown": ["shutdown"],
            "lock": ["lock"],
            "terminal": ["terminal"],
            "input source": ["input_source"],
            # 04-Process: trading & quant
            "backtest": ["strategy_backtest"],
            "backtesting": ["strategy_backtest"],
            "trading strategy": ["strategy_backtest"],
            "quantitative": ["strategy_backtest"],
            "stock trading": ["strategy_backtest"],
            # 04-Process: memory backup
            "memory backup": ["memory_backup"],
            "memory restore": ["memory_backup"],
            "backup memory": ["memory_backup"],
            "backup my": ["memory_backup"],
            "scheduled backup": ["memory_backup"],
            "chat memory": ["memory_backup"],
        }
        
        for keyword, skills in skill_keywords.items():
            # Word-boundary matching to avoid false positives (e.g. "open" in "OpenClaw", "ip" in "script")
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, demand_lower):
                for skill in skills:
                    if skill not in [d["skill"] for d in decomposed]:
                        decomposed.append({
                            "skill": skill,
                            "confidence": 0.8,
                            "matched_keyword": keyword
                        })
        
        # If no skills matched, return the original demand
        if not decomposed:
            decomposed.append({
                "skill": "unknown",
                "confidence": 0.0,
                "original_demand": demand
            })
        
        return decomposed
    
    def to_markdown(self, demand, decomposed):
        """Convert decomposition result to markdown"""
        result = f"# Decomposition Result\n\n"
        result += f"## Original Demand\n{demand}\n\n"
        result += f"## Decomposed Skills\n"
        
        for item in decomposed:
            result += f"- **{item['skill']}** (confidence: {item.get('confidence', 0)})\n"
            if "matched_keyword" in item:
                result += f"  - Matched by keyword: {item['matched_keyword']}\n"
            elif item.get("source") == "llm":
                result += f"  - From LLM decomposition\n"
            if "original_demand" in item:
                result += f"  - No matching skills found\n"
        
        return result


def _decompose_llm(demand: str, model: str = None) -> list:
    """LLM-powered decomposition via Chutes or OpenAI. Falls back to [] on error."""
    try:
        from config import get_llm_client, has_llm
        if not has_llm():
            return []
        client, default_model = get_llm_client()
        if not client:
            return []
        use_model = model or default_model
        prompt_path = Path(__file__).parent.parent / "prompts" / "gpt" / "main.txt"
        prompt_tpl = prompt_path.read_text() if prompt_path.exists() else "Decompose: {human_demand}"
        prompt = prompt_tpl.replace("{human_demand}", demand)
        r = client.chat.completions.create(
            model=use_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=1024,
        )
        text = r.choices[0].message.content or ""
        return _parse_llm_skills(text) if text else []
    except Exception:
        return []


def _parse_llm_skills(text: str) -> list:
    """Parse LLM output into skill list."""
    decomposed = []
    for line in text.split("\n"):
        m = re.search(r"-\s+(?:\*\*?)?([a-zA-Z0-9_\s-]+?)(?:\*\*?)?(?:\s*:|$)", line)
        if m:
            sk = m.group(1).strip().lower().replace(" ", "_").replace("__", "_")
            if sk and sk not in ("description", "category", "difficulty") and len(sk) > 2:
                decomposed.append({"skill": sk, "confidence": 0.9, "source": "llm"})
    return decomposed


class CutterEngine:
    """Main cutter engine for demand processing"""
    
    def __init__(self):
        self.decomposer = Decomposer()
        self.version = "1.0.0"
    
    def process(self, demand, skill_index_content=None, model: str = None):
        """
        Process a human demand.
        If model is 'gpt' and OPENAI_API_KEY set, use LLM; else keyword matching.
        """
        if skill_index_content:
            self.decomposer.load_skill_index(skill_index_content)
        
        decomposed = []
        if model and model.lower() in ("gpt", "chutes", "llm"):
            decomposed = _decompose_llm(demand, model=model)
        if not decomposed:
            decomposed = self.decomposer.decompose(demand)
        
        return {
            "version": self.version,
            "demand": demand,
            "decomposed": decomposed,
            "markdown": self.decomposer.to_markdown(demand, decomposed)
        }


# Alias for __init__.py
Cutter = CutterEngine


# CLI interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python cutter.py <demand>")
        sys.exit(1)
    
    demand = " ".join(sys.argv[1:])
    engine = CutterEngine()
    result = engine.process(demand)
    print(result["markdown"])

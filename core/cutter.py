"""
MetaSkillBase Core - Cutter Engine
Demand decomposition and skill extraction engine
"""

import json
import re


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
        }
        
        for keyword, skills in skill_keywords.items():
            if keyword in demand_lower:
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
            result += f"- **{item['skill']}** (confidence: {item['confidence']})\n"
            if "matched_keyword" in item:
                result += f"  - Matched by keyword: {item['matched_keyword']}\n"
            if "original_demand" in item:
                result += f"  - No matching skills found\n"
        
        return result


class CutterEngine:
    """Main cutter engine for demand processing"""
    
    def __init__(self):
        self.decomposer = Decomposer()
        self.version = "1.0.0"
    
    def process(self, demand, skill_index_content=None):
        """
        Process a human demand
        
        Args:
            demand: Human-readable demand string
            skill_index_content: Optional skill index content
            
        Returns:
            dict with decomposition result
        """
        if skill_index_content:
            self.decomposer.load_skill_index(skill_index_content)
        
        decomposed = self.decomposer.decompose(demand)
        
        return {
            "version": self.version,
            "demand": demand,
            "decomposed": decomposed,
            "markdown": self.decomposer.to_markdown(demand, decomposed)
        }


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

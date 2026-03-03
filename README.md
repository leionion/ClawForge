# MetaSkillBase-Core
## Meta Skill Library for Demand Decomposition & OpenClaw Ecosystem

A universal, open, and elastic meta skill ecosystem that decomposes human demands into reusable atomic meta skills — **One for Human, One for Bot**.

---

## One for Human, One for Bot — The Deeper Meaning

**We believe: Every product in the world — both software and hardware — will need two kinds of "instructions":**

1. **One for Human**: User manual, guides, documentation
2. **One for Bot**: Machine-readable instructions that AI can understand and execute

This is not just about documentation. This is about **making every product AI-controllable**.

**Real example:**
- Your air conditioner has HomeKit
- **One for Human**: Remote control manual
- **One for Bot**: Air conditioner Meta Skill → OpenClaw can control it

**The vision:** A world where every product has both — readable by humans, executable by AI. This is the future Meta Skill enables.

---

## The Real Story: Why We Need Meta Skills

**Problem:**
I asked my Mac mini to upgrade OpenClaw. It said: *"I can't. No permission."*

**Conversation:**
> **OpenClaw:** I've run Terminal. You can input the password now.
> 
> **Me:** I can't see where to input the password. You need to activate Terminal in a way that I can see.
> 
> **OpenClaw:** Got it! Using `mac_activate` to bring Terminal to the foreground.
> 
> **Me:** Now I can see it. Let me enter the password... Done!
> 
> **OpenClaw:** Upgrade complete! ✅

**Result:** OpenClaw upgraded through human-machine collaboration.

---

### Why This Matters

1. **Machines prefer background silent execution** — but AI solving real problems often requires human-machine collaboration
2. **This is just ONE case** — Mac operations need: activate app, run terminal, adjust volume, take screenshot, lock screen... → **30+ Meta Skills**
3. **The finer the decomposition, the easier the development**
   - Complex demand → Simple Meta Skills → Easy to build, easy to combine
4. **Human's role:** Describe the demand
   - **Meta Skills' role:** Provide atomic capabilities
   - **OpenClaw's role:** Execute and solve

---

## Our Vision

**We believe:**
- Every human — regardless of technical knowledge — should be able to ask OpenClaw to solve problems.
- No need to understand code, commands, or systems.
- **You only need to describe what you want.**

**Through continuous decomposition (Cutter):**
```
Your Demand → Cutter → Atomic Meta Skills → OpenClaw Executes → Problem Solved
```

**The result:**
- **Humans** focus on *describing needs*
- **Meta Skills** provide *atomic capabilities* (basic skill units)
- **OpenClaw** handles *execution*
- Every human's problem can be solved

**This is our vision:** A world where anyone can change the world through OpenClaw — not by knowing technology, but by having the willingness to solve problems.

---

OpenClaw has built a complete Skill system.
We found that most skills can be further decomposed into finer, reusable, professional basic units.

Therefore, we define:
- **Meta Skill**: Supply-oriented, developer-facing, atomic, reusable finest-grained functional component.

We focus on the OpenClaw ecosystem. We follow its skill system and standards to build and provide Meta Skills, and contribute to the OpenClaw community.

### Current Status
- Framework and architecture: defined
- Core specification: defined
- Meta Skill collection: in progress (仓库建设中)
- Cutter engine: in development
- Community: welcome contributors

### Skill Hierarchy
```
Human Demand
    ↓
OpenClaw
    ↓
Meta Skill       ←───── MetaSkillBase-Core
```

- **Meta Skill**: Finest-grained reusable functional component.

### Core Value
1. **Supply-Driven**: Every Meta Skill is a valuable "supply" — the more, the better
2. **Demand-Responsive**: Every demand can be decomposed and fulfilled
3. **Open Collaboration**: Anyone can contribute — no rejection, no audit
4. **Human-Bot Symbiosis**: Humans describe needs; machines execute solutions

### Repository Structure
```
MetaSkillBase-Core/
├── skills/                    # Core meta skill library
│   ├── 00-Unclassified/
│   ├── 01-Base/
│   ├── 02-Device/
│   ├── 03-Manual/
│   ├── 04-Process/
│   └── 05-Interaction/
├── core/                     # Cutter Engine
├── prompts/                  # Prompts for Cutter
├── data/                     # Ecosystem data
└── docs/                     # Documentation
```

### Cutter Engine
A demand decomposition and skill search tool for OpenClaw, mapping human natural language demands into atomic Meta Skills.

**Flow:**
```
User Demand → Cutter →
  1. Search OpenClaw
  2. Query local Skills
  3. Search MetaSkillBase-Core → Meta Skills
  4. Submit Demand (if missing)
```

**Output:**
- Existing Meta Skills that match the demand
- Missing Meta Skills that need development

### Quick Start
```bash
cd MetaSkillBase-Core
pip install -r requirements.txt
python -m core.cutter "Your human demand here" --model gpt
```

### Community Rules
- No Rejection: Any skill or demand can be submitted.
- Open Collaboration: Fork, PR, Issue.
- Quality Focus: Useful and reliable.

### License
Apache License 2.0

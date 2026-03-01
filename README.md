# MetaSkillBase-Core
## Atomic Meta Skill Library for Human-Bot Symbiosis
A universal, open, and elastic meta skill ecosystem that decomposes human demands into reusable atomic meta skills—One for Human, One for Bot.


This repository is the official core of the MetaSkillBase open-source community, providing a complete set of standards, tools, and community rules for building, classifying, and reusing meta skills across all bot/agent ecosystems.


### Current Status
MetaSkill Base Core is in early development stage.
- Framework and architecture: complete
- Core specification: defined
- Meta Skill collection: in progress
- Cutter engine: under development
- Pre-release community project: contributions welcome


### Core Value
1. Elastic Classification: Classification as inspiration, not restriction—no rejection, no audit, only organization.
2. Dual Contributor System: Equal respect for Demand Contributors (DC) and Skill Implementers (SI).
3. Human-Bot Symbiosis: Humans define high-value demands, bots execute via composable meta skills.
4. Open Growth: Continuously expand the meta skill library through community collaboration, with Usage Count as the core value metric.


### Repository Structure
```
MetaSkillBase-Core/
├── skills/          # Core meta skill library (classified)
│   ├── 00-Unclassified/  # Default for unclassified skills
│   ├── 01-Base/          # Fundamental atomic operations
│   ├── 02-Device/        # Device & system operations
│   ├── 03-Manual/        # Machine-readable manuals
│   ├── 04-Process/       # Enterprise process units
│   └── 05-Interaction/   # Human-bot collaboration actions
├── core/            # Cutter Engine - Demand decomposition core
├── prompts/         # Model-specific prompts for Cutter
├── data/            # Auto-updated ecosystem data
├── curation/        # Skill curation for other communities
└── docs/            # Official documentation (Glossary/Core Rules)
```


### Key Components
#### 1. Cutter Engine
The core tool that decomposes human natural language demands into atomic meta skills. It supports:
- Demand parsing & classification
- Model-specific prompt evolution
- Contribution recording & ecosystem analytics
- One-click adaptation to any bot community (via Head Layer)


#### 2. Standard Documents
All core rules and standards are defined in the official docs (root directory):
- **Glossary.md**: Global terminology for the MetaSkillBase ecosystem
- **MetaSkillBase-Core.md**: Core classification, repository rules & contribution principles
- **MetaSkillBase-Index.md**: Global skill index & usage statistics
- **Demand-Board.md**: Demand submission & implementation rules


### Quick Start
#### 1. Local Setup
```bash
cd MetaSkillBase-Core
```
#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
#### 3. Run Cutter Engine (Demand Decomposition)
```bash
python -m core.cutter "Your human demand here" --community openclaw --model gpt
```


### Community Rules
- No Rejection: Any skill or demand can be submitted—we only organize, not judge.
- Equal Respect: DC and SI are both the core of the ecosystem, with Usage Count as the core reward.
- Open Collaboration: Fork the repo, submit PRs for meta skills/Cutter improvements, create Issues for new demands.


### Contribution Guide
See CONTRIBUTING.md for detailed rules on submitting demands, developing meta skills, and contributing to the Cutter Engine.


### License
This project is licensed under the Apache License 2.0—see LICENSE for details.


### Core Team
MetaSkillBase Team - Building the future of human-bot symbiosis through open, reusable meta skills.

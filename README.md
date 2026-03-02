================================================================================



# MetaSkillBase-Core

## Meta Skill Library for Demand Decomposition & OpenClaw Ecosystem



A universal, open, and elastic meta skill ecosystem that decomposes human demands into reusable atomic meta skills—One for Human, One for Bot.



We focus on the OpenClaw ecosystem. We follow its skill system and standards to build Bot Skills and Meta Skills, and contribute to the OpenClaw community and human-bot symbiosis.



### Current Status

- Framework and architecture: complete

- Core specification: defined

- Meta Skill collection: in progress

- Cutter engine: stable (P0 completed)

- Community: active and growing



### Skill Hierarchy

Bot Skills are assembled from Meta Skills. Meta Skills are the atomic building blocks of Bot automation.


```

Human Demand (人类需求)

    ↓

OpenClaw (机器人)

    ↓

Bot Skill (机器人技能) ←─── OpenClaw社区

    ↓

Meta Skill (元技能) ←───── MetaSkillBase-Core

```



- **Meta Skill**: Finest-grained reusable functional component. The finer the decomposition, the easier and more stable development becomes.
- **Bot Skill**: High-level solution assembled from Meta Skills, enabling rich and flexible automation.



### Core Value

1. Elastic Classification: Classification as inspiration, not restriction—no rejection, no audit, only organization.

2. Open Collaboration: Built by contributors, for the community.

3. Human-Bot Symbiosis: Humans define high-value demands, bots execute via composable meta skills.

4. Usage Count is a community metric reflecting skill value, recorded and maintained by contributors.



### Repository Structure

```

MetaSkillBase-Core/

├── skills/                    # Core meta skill library

│   ├── 00-Unclassified/      # Default for unclassified skills

│   ├── 01-Base/              # Fundamental atomic operations

│   ├── 02-Device/            # Device & system operations

│   ├── 03-Manual/            # Machine-readable manuals

│   ├── 04-Process/           # Enterprise process units

│   └── 05-Interaction/       # Human-bot collaboration actions

├── core/                     # Cutter Engine

├── prompts/                  # Model-specific prompts for Cutter

├── data/                     # Auto-updated ecosystem data

└── docs/                     # Official documentation

```



### Key Components



#### 1. Cutter Engine



A demand decomposition and skill search tool dedicated for OpenClaw, which maps human natural language demands into atomic, combinable Meta Skills.



**Simple Flow:**

```

User Demand → Cutter → 

  1. Search OpenClaw → Bot Skills

  2. Query Local Skills

  3. Search MetaSkillBase-Core → Meta Skills

  4. Submit Demand (if missing)

```



**Output:**

- Bot Skills that fully meet the demand

- Bot Skills that partially meet + missing Meta Skills

- Missing Meta Skills ready for development



#### 2. Standard Documents

All core rules and standards are defined in the official docs:

- **Glossary.md**: Global terminology for the MetaSkillBase ecosystem

- **MetaSkillBase-Core.md**: Core classification, repository rules & contribution principles

- **Skill-Index.md**: Global skill index & usage statistics

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

#### 3. Run Cutter Engine

```bash

python -m core.cutter "Your human demand here" --model gpt

```



### Community Rules

- No Rejection: Any skill or demand can be submitted—we only organize, not judge.

- Open Collaboration: Fork the repo, submit PRs, create Issues.

- Quality Focus: Every skill should be useful and reliable.



### Contribution Guide

See CONTRIBUTING.md for detailed rules on submitting demands, developing meta skills, and contributing to the Cutter Engine.



### License

This project is licensed under the Apache License 2.0—see LICENSE for details.



### Core Team

MetaSkillBase-Core Team - Building the future of human-bot symbiosis through open, reusable meta skills.





---

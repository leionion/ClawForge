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



# README.md 中文翻译



# MetaSkillBase-Core

## 面向需求拆解的元技能库・服务 OpenClaw 生态



一个通用、开放、灵活的元技能生态系统，将人类需求分解为可复用的原子化元技能——一人一机，相互协作。



我们聚焦 OpenClaw 生态，遵循其技能体系与标准，构建机器人技能与元技能，为 OpenClaw 社区与人机共生贡献价值。



### 当前状态

- 框架与架构：已完成

- 核心规范：已定义

- 元技能集合：持续更新中

- Cutter引擎：已完成P0

- 社区：活跃且不断成长



### 技能层级结构



```

人类需求 (Human Demand)

    ↓

OpenClaw (机器人)

    ↓

Bot Skill (机器人技能) ←─── OpenClaw社区

    ↓

Meta Skill (元技能) ←───── MetaSkillBase-Core

```



- **Bot Skill**：由多个Meta Skill组成的复杂技能

- **Meta Skill**：形成Bot Skill的原子化可复用技能单元



### 核心价值

1. 弹性分类：分类即灵感，非限制——无拒绝、无审核、仅组织

2. 开放协作：由贡献者构建，为社区服务

3. 人机共生：人类定义高价值需求，机器人通过可组合的元技能执行

4. 使用次数是反映技能价值的社区指标，由社区贡献者记录与维护。



### 仓库结构

```

MetaSkillBase-Core/

├── skills/                    # 核心元技能库

│   ├── 00-Unclassified/      # 未分类技能默认位置

│   ├── 01-Base/              # 基础原子操作

│   ├── 02-Device/            # 设备与系统操作

│   ├── 03-Manual/            # 机器可读手册

│   ├── 04-Process/           # 企业流程单元

│   └── 05-Interaction/       # 人机协作动作

├── core/                     # Cutter引擎

├── prompts/                  # Cutter模型特定提示词

├── data/                     # 自动更新的生态系统数据

└── docs/                     # 官方文档

```



### 关键组件



#### 1. Cutter引擎



在社区间搜索技能以满足人类需求的核心工具。



**简单流程：**

```

用户需求 → Cutter →

  1. 搜索OpenClaw → Bot Skills

  2. 查询本地Skills

  3. 搜索MetaSkillBase-Core → Meta Skills

  4. 提交需求（如有缺失）

```



**输出：**

- 完全满足需求的Bot Skills

- 部分满足的Bot Skills + 缺失的Meta Skills

- 准备开发的缺失Meta Skills



#### 2. 标准文档

所有核心规则和标准都定义在官方文档中：

- **Glossary.md**：MetaSkillBase生态系统术语表

- **MetaSkillBase-Core.md**：核心分类、仓库规则与贡献原则

- **Skill-Index.md**：全球技能索引与使用统计

- **Demand-Board.md**：需求提交与实施规则



### 快速开始

#### 1. 本地设置

```bash

cd MetaSkillBase-Core

```

#### 2. 安装依赖

```bash

pip install -r requirements.txt

```

#### 3. 运行Cutter引擎

```bash

python -m core.cutter "你的需求" --model gpt

```



### 社区规则

- 无拒绝：任何技能或需求都可以提交——我们只组织，不评判

- 开放协作：Fork仓库，提交PR，创建Issue

- 质量focus：每个技能都应该有用且可靠



### 贡献指南

关于提交需求、开发元技能和为Cutter引擎贡献的详细规则，请参阅CONTRIBUTING.md。



### 许可证

本项目采用Apache License 2.0——详见LICENSE文件。



### 核心团队

MetaSkillBase-Core团队 - 通过开放、可复用的元技能构建人机共生未来





================================================================================

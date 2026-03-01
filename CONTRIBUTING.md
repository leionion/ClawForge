# Contributing to MetaSkillBase-Core
Thank you for your interest in contributing to MetaSkillBase-Core! This document outlines the rules and workflows for contributing to our ecosystem—every contribution, big or small, is valuable.


MetaSkillBase-Core follows the Open Collaboration Principle: no rejection, no audit, only organization. All contributions (demands, meta skills, code, docs) are welcome as long as they align with our core philosophy: One for Human, One for Bot.


## Who Can Contribute?
- Demand Contributor (DC): Anyone who submits high-value, actionable human demands for bot skills.
- Skill Implementer (SI): Anyone who develops and submits atomic meta skills.
- Code Contributor: Anyone who improves the Cutter Engine, fixes bugs, or adds new features.
- Doc Contributor: Anyone who updates documentation, corrects typos, or adds examples.


## Contribution Workflows
### 1. Submit a New Demand (Become a DC)
Follow the rules in Demand-Board.md for full details—core steps:
1. Create a new Issue in the repository.
2. Title format: Demand: [Skill Name] – [Function Description] (e.g., Demand: expect – Handle interactive input for sudo).
3. Describe the demand clearly: what the bot should accomplish, use cases, and expected behavior.
4. Add the label: demand.
5. You will be marked as the DC for this demand once the Issue is created.


### 2. Develop a Meta Skill (Become a SI)
1. Choose an existing Issue with the demand label (unclaimed).
2. Comment on the Issue to claim it (avoid duplicate development).
3. Develop the meta skill following our Atomic Rule: one skill = one minimal, reusable function.
4. Follow the MetaSkillBase-Core.md classification rules to place the skill in the correct skills/[category] directory.
5. Create a new PR with the skill file (Markdown + executable code if applicable).
6. PR title format: SI: [Skill Name] – [Category] (e.g., SI: expect – 05-Interaction).
7. You will be marked as the SI for this skill once the PR is merged.


### 3. Contribute to the Cutter Engine (Code Contribution)
1. Follow standard code development practices.
2. Follow the Python PEP 8 code style for all code changes.
3. Add comments for core logic and new features (ensure readability).
4. Test your changes locally to avoid breaking the core Cutter functionality.


### 4. Update Documentation (Doc Contribution)
1. Update the relevant Markdown file (Glossary.md/MetaSkillBase-Core.md/etc.).
2. Ensure the documentation is clear, concise, and consistent with the project's core terminology.


## Contribution Standards
### 1. Meta Skill Standards
- Atomicity: One meta skill must implement only one minimal, reusable function (no complex composite logic).
- Naming: Use lowercase letters and hyphens for skill names (e.g., expect, http-client).
- Documentation: Each skill must have a Markdown file with: skill name, description, usage, and input/output format.
- Classification: Strictly follow the MetaSkillBase-Core.md category rules—place unclassified skills in skills/00-Unclassified.


### 2. Code Standards
- Follow Python PEP 8 for all Cutter Engine code.
- Use meaningful variable/function/class names (avoid abbreviations unless universally recognized).
- Add docstrings for all functions/classes (Google style recommended).
- Do not add unnecessary third-party dependencies (keep the Cutter Engine light).


### 3. Communication Standards
- Be respectful and friendly in all discussions.
- Respond to comments in a timely manner.
- Avoid off-topic discussions—focus on the contribution itself.


## Reward & Recognition
All contributions are recorded in the MetaSkillBase-Index.md with the contributor's GitHub ID:
- Demand Contributors (DC): Your ID is linked to every demand you submit—Usage Count of the skill will reflect your contribution value.
- Skill Implementers (SI): Your ID is linked to every meta skill you develop—Usage Count is the core reward for your work.


The higher the Usage Count of the skill/demand you contribute, the greater your impact on the MetaSkillBase ecosystem!


## Questions & Support
If you have any questions about contributing, create a new Issue with the label question—our core team and community will help you!


Thank you for building the MetaSkillBase ecosystem with us! 🚀

"""Setup for pip install -e ."""
from setuptools import setup, find_packages

setup(
    name="openclaw-skill-forge",
    version="0.2.0-beta",
    description="OpenClaw Skill Forge — Decompose demands into AI skills. For traders & developers.",
    py_modules=["metaskill_cli", "config"],
    packages=find_packages(include=["core"]),
    include_package_data=True,
    package_data={"": ["skills/**/*", "prompts/**/*", "data/*.json"]},
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "streamlit>=1.28.0",
        "openai>=1.0.0",
    ],
    entry_points={"console_scripts": ["metaskill=metaskill_cli:main"]},
)

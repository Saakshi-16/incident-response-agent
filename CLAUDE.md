# Project: Incident Response Agent

See README.md for what this project is and the phase roadmap.

## About me
I am learning to work as a professional engineer. My goal is to
UNDERSTAND everything, not just get working code.

## How to work with me
- Before writing code, explain the plan in simple words and wait for my OK.
- Work in small steps: one feature or file at a time.
- After each change, explain what each new file, function or config does and why.
- When you introduce a new tool or concept, explain it briefly with an analogy.
- If I ask "why", explain the concept, not just the code.
- Do NOT run git commit or git push. Suggest the commit message and let me run it.
- If something I ask for is a bad practice, tell me and explain why.

## Environment
- Ubuntu on WSL2 (Windows laptop). Docker Desktop with WSL integration.
- Limited RAM for Docker (~3.5 GB): prefer lightweight setups.
- Python 3.12 managed with uv (use `uv add`, `uv run`; never `pip install` into system Python).

## Code standards
- Type hints on all functions.
- Format and lint with ruff.
- Every function in agent/tools/ must have a pytest test.
- Never hardcode secrets. Read them from environment variables (.env, which is git-ignored).
- Use structured (JSON) logging, not print().
- All timestamps in UTC.
- Conventional Commits for messages: feat:, fix:, docs:, chore:, test:, refactor:

## Safety rules for the agent (Phases 5–7)
- Investigation agents are read-only.
- Actions only from an explicit allowlist, enforced in code.
- Human approval is enforced in code, never only in the prompt.
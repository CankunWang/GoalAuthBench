# GoalAuthBench

> Status: Gate 0 — repository bootstrap. No experimental results are available yet.

GoalAuthBench is a controlled authorization and shortcut audit for LLM agents. It evaluates authorized and unauthorized contexts against the same canonical tool call and typed arguments, then measures which monitors remain useful after source and surface shortcuts are controlled.

## Scope

- Versioned authorization, provenance, lineage, and canonical-action schemas
- Exact-action matched data with leakage validation
- Deterministic, text, provenance, counterfactual, and optional latent baselines
- Pre-registered grouped out-of-distribution evaluation
- A policy-first T2 pre-commit gate for side-effecting tool calls

The first release does not claim to solve prompt injection or provide a production authorization system. Hidden-state, multilingual, and adaptive-attack experiments remain conditional extensions.

## Quickstart

Requirements:

- Python 3.11
- [uv](https://docs.astral.sh/uv/)

```powershell
uv sync --frozen
uv run python -c "import goalauthbench"
uv build
```

## Current phase

The project is establishing its package, research protocol, threat model, label guide, tests, and continuous-integration checks. Planned work must not be interpreted as completed functionality.

The current execution baseline is [`GoalAuthBench_v0.2_重审执行版_2026-07-27.md`](./GoalAuthBench_v0.2_重审执行版_2026-07-27.md).


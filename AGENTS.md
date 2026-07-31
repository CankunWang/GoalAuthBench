# GoalAuthBench Agent Rules

## Clarify

- If any requirement, scope, research meaning, security boundary, output, or acceptance criterion is unclear, stop immediately and ask the project owner. Do not guess. State the ambiguity, its impact, and the minimum decision required.

## Authority

- Accepted files in `docs/adr/` govern recorded architecture decisions.
- `docs/research/threat-model.md` governs security boundaries; `docs/research/label-guide.md` governs labels and decision semantics.
- `GoalAuthBench_v0.2_重审执行版_2026-07-27.md` governs remaining research scope where it is not superseded by an accepted ADR or research baseline.
- `docs/planning/GoalAuthBench_工程级项目标准与参考建议_v0.1.md` governs implementation quality; `docs/archive/GoalAuthBench_整体方案重审报告_2026-07-27.md` provides rationale only.
- Historical plans and past conversations are context only; persist approved decisions in repository files.

## Iron Rules

- Do not change labels, authorization semantics, policy, primary metrics or splits, threat-model boundaries, release claims, or v1 scope without owner approval.
- Treat the LLM and external content as untrusted; keep authorization, state, and utility oracles separate.
- An explicit `DENY` is never overridable. Evaluated runtime side effects must pass through the T2 pre-commit boundary.
- Do not present planned, partial, failed, or unverified work as complete.
- Preserve formal experiment failures, invalid runs, negative results, and known limitations.
- Address only the requested task; exclude unrelated modifications.

## Commands

```text
uv sync --frozen
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
uv build
```

## Approval and Completion

- Ask before spending money, publishing or releasing, using real credentials, personal data, production resources or non-public restricted materials, deleting or replacing project data or research documents, changing frozen research decisions, adding a framework, or expanding v1 scope.
- Run all applicable checks and report their actual results. Do not claim completion while any stated acceptance criterion remains unverified.

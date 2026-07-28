# GoalAuthBench Agent Instructions

## 1. Clarify First

- If any requirement, scope, research meaning, security boundary, expected output, or acceptance criterion is unclear, stop immediately and ask the project owner.
- Do not guess, silently choose an interpretation, or continue with assumptions that could change the result.
- When asking, state what is unclear, why it matters, and the smallest decision needed to continue.

## 2. Source of Truth

- `GoalAuthBench_v0.2_重审执行版_2026-07-27.md` is the current execution baseline.
- `GoalAuthBench_整体方案重审报告_2026-07-27.md` explains the decisions behind the current baseline.
- `GoalAuthBench_工程级项目标准与参考建议_v0.1.md` defines the engineering and research-quality requirements.
- If these documents conflict, v0.2 governs research scope and semantics; the engineering standard governs implementation quality; the review report provides rationale only.
- Other project plans are historical context and must not override these sources.
- Conversation content is not a persistent source of truth unless written back to the repository.

## 3. Change Boundaries

- Do not change research labels, authorization semantics, policy rules, primary metrics, primary splits, threat-model boundaries, or release claims without explicit approval from the project owner.
- Do not expand the v1 scope defined in section 1 of the v0.2 execution baseline without explicit approval.
- Do not present planned, partial, or unverified work as completed.
- Each change must address the requested task and exclude unrelated modifications.

## 4. Safety and Research Integrity

- Treat the LLM and external content as untrusted.
- Keep authorization, environment state, and task utility as separate oracles.
- An explicit `DENY` must never be overridden by a learned detector.
- In the evaluated Agent runtime, every side-effecting tool call must pass through the T2 pre-commit policy enforcement boundary.
- Do not use real credentials, personal data, production systems, or non-public restricted materials without explicit approval from the project owner.
- Preserve failures, invalid runs, negative results, and known limitations from formal experiments and published evaluations.

## 5. Verification

- Every implementation change must satisfy the task's acceptance criteria with tests or reproducible verification evidence.
- Report commands actually run and their real results.
- Do not silently skip failing checks.
- Do not claim completion while any stated acceptance criterion remains unverified.

## 6. Actions Requiring Approval

Ask before:

- using paid APIs or spending money;
- publishing externally or creating a release;
- using real credentials or external production resources;
- deleting or replacing project data or research documents;
- changing frozen research decisions;
- adding a framework dependency or expanding the v1 scope defined in the current execution baseline.

# ADR-0001: T2 Pre-commit Enforcement Boundary

> Status: Accepted
> Date: 2026-07-29
> Decision owner: Project owner

## Context

GoalAuthBench must evaluate a complete candidate tool call without allowing the evaluated
side effect to occur first. Checking before the complete arguments exist cannot bind the
actual effect; checking after execution cannot prevent it.

## Decision

The primary enforcement boundary is `T2`:

```text
T0 external content read
T1 tool name generated
T2 complete call buffered, parsed, canonicalized, and not yet dispatched
T3 external effect attempted or applied
```

Every registered side-effecting tool must enter the PEP at `T2`. The PEP approves an
immutable authorization envelope, not raw model text. The executor accepts only a
`PREPARED` envelope whose digest, account, principal, session, policy, provenance, quota,
and schema bindings remain unchanged.

Policy `PERMIT` maps to `COMMIT`; `DENY`, `NO_MATCH`, and `INVALID` map to `BLOCK`;
structured `CONFIRM_REQUIRED` maps to `WOULD_CONFIRM` without dispatch. A semantic
`AMBIGUOUS` delegation label does not itself open a confirmation path.

## Consequences

- Complete mediation and PEP-to-executor binding become mandatory integration-test targets.
- Teacher-forced analysis at `T2` is an audit of signals, not evidence of natural model
  behavior.
- Natural rollout must report proposed, blocked, committed, and externally observed
  effects separately.
- External services may prevent true distributed atomicity, so the implementation uses a
  durable preparation state, idempotency key, and reconciliation rather than claiming an
  unsupported transaction guarantee.
- A side effect that bypasses `T2` is a security failure.

## References

- [Threat model](../research/threat-model.md)
- [GoalAuthBench v0.2](../../GoalAuthBench_v0.2_重审执行版_2026-07-27.md)

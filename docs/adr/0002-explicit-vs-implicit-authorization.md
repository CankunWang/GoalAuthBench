# ADR-0002: Separate Explicit Policy from Implicit Delegation

> Status: Accepted
> Date: 2026-07-29
> Decision owner: Project owner

## Context

An authenticated user can submit a request containing quotations, forwarded content,
attachments, or retrieved text. Treating every token from that channel as authorization
would allow embedded untrusted content to manufacture authority.

GoalAuthBench also needs to study natural-language delegation without allowing uncertain
semantic judgments to become the sole execution boundary.

## Decision

GoalAuthBench maintains two tracks:

- **Track E — explicit policy:** structured policy and authorization manifests are the only
  sources that can grant executable permission. A deterministic PDP/PEP is authoritative.
- **Track I — implicit delegation:** natural-language goals, provenance, and authorization
  witnesses are research evidence. Its semantic result is a `delegation_label`.

Authentication establishes the origin, principal, and session of a user request. It does
not make all request text authoritative. Textual evidence cannot create a dispatchable
policy permission.

GoalAuthBench records three independent layers:

```text
delegation_label:
  SUPPORTED | UNSUPPORTED | AMBIGUOUS

policy_decision:
  PERMIT | DENY | CONFIRM_REQUIRED | NO_MATCH | INVALID

gate_decision:
  COMMIT | BLOCK | WOULD_CONFIRM
```

For v1 enforcement:

- `PERMIT` may reach `COMMIT`;
- `DENY`, `NO_MATCH`, and `INVALID` produce `BLOCK`;
- structured `CONFIRM_REQUIRED` produces `WOULD_CONFIRM` and does not dispatch;
- `delegation_label` never directly controls execution.

Learned semantic, counterfactual, or latent signals may support auditing and risk routing.
They cannot create authority or override structured policy.

## Consequences

- Delegation labels, policy decisions, and Gate decisions must be represented separately.
- Track I remains useful for measurement even though it cannot independently authorize
  execution.
- The label guide must define `SUPPORTED`, `UNSUPPORTED`, and `AMBIGUOUS` without silently
  converting uncertain cases to binary labels.
- Proposal safety and enforcement safety require separate metrics.

## References

- [Threat model](../research/threat-model.md)
- [Label guide](../research/label-guide.md)
- [GoalAuthBench v0.2](../../GoalAuthBench_v0.2_重审执行版_2026-07-27.md)

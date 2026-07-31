# Security Requirements Traceability

> Status: Gate 0 specification
> Last reviewed: 2026-07-29
> Implementation evidence is not yet available unless explicitly stated.

This matrix connects each security requirement to its planned automated test and required
evidence. A planned test is not evidence that the requirement has been implemented.

| ID | Security requirement | Planned verification | Required evidence | Current status |
| --- | --- | --- | --- | --- |
| SR-001 | `DENY`, `NO_MATCH`, and `INVALID` never dispatch | Golden and integration test | Gate event, no executor call, unchanged state | Specified |
| SR-002 | Only structured `CONFIRM_REQUIRED` becomes `WOULD_CONFIRM` | Golden test | Three-layer decision trace and unchanged state | Specified |
| SR-003 | Missing policy and all failed preconditions block | Parameterized unit/property tests | Failure reason for every policy-decision row | Specified |
| SR-004 | Every side-effecting route passes through the T2 PEP | Registry integration test | Route inventory and PEP trace | Specified |
| SR-005 | Unregistered or incomplete side-effecting tools fail CI | Negative registry test | Deliberately incomplete fixture rejected | Specified |
| SR-006 | Executor accepts only a prepared immutable envelope | Integration/property tests | State transition and executor rejection trace | Specified |
| SR-007 | Committed and dispatched envelope bindings are identical | Mutation/property tests | Both digests and bound-field diff | Specified |
| SR-008 | Quota and nonce are reserved with durable audit intent | State-machine integration test | Atomic-store transaction record | Specified |
| SR-009 | Retry cannot duplicate an external effect | Idempotency integration test | Stable key and single state effect | Specified |
| SR-010 | Email fields are completely canonicalized and authorized | Schema/golden/property tests | Canonical fixture and policy decision | Specified |
| SR-011 | Calendar fields are completely canonicalized and authorized | Schema/golden/property tests | Canonical fixture and policy decision | Specified |
| SR-012 | Unknown, extra, ambiguous, or lossy fields block | Fuzz/property tests | Rejected input and reason code | Specified |
| SR-013 | Textual trust claims cannot create authority | Matched golden test | Same call, different operational provenance | Specified |
| SR-014 | Static attacks remain frozen during primary evaluation | Manifest validator | Attack/version hash and pre-test timestamp | Specified |
| SR-015 | Proposal and committed-action metrics remain separate | Hand-calculated metrics fixture | Expected and computed metric values | Specified |
| SR-016 | Security failure and experimental validity remain orthogonal | Classification unit test | Cases covering all outcome combinations | Specified |
| SR-017 | Only declared business quotas are protected in v1 | Policy/schema test | Quota dimensions in manifest and decisions | Specified |
| SR-018 | Delegation, policy, and Gate decisions remain separate | Classification/property test | Three independent fields for every fixture | Specified |
| SR-019 | Every label has reason codes, witness, provenance, and versioned review evidence | Label validator | Complete label record and adjudication history | Specified |

## Evidence rules

- `Specified` means the requirement is documented but not implemented.
- `Implemented` requires reviewed code and an identified test.
- `Verified` requires a passing test result bound to a commit SHA and CI run.
- Missing evidence must not be inferred from passing unrelated tests.
- Security failures, invalid runs, negative results, and `UNKNOWN` execution states must be
  retained.

## Authority

- [Threat model](./threat-model.md)
- [Label guide](./label-guide.md)
- [ADR-0001](../adr/0001-t2-precommit-boundary.md)
- [ADR-0002](../adr/0002-explicit-vs-implicit-authorization.md)

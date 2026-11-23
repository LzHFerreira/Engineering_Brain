# Engineering Brain

**Status — Architecture proposal. Implementation and benchmark results are pending.**

Enable small local models to make and verify ordinary code changes as the repository grows. Design each task to fit within one cohesive module, its public contracts, immediate dependencies, and focused tests. The proposal is language-agnostic.

## Architecture

Start with a **modular monolith**. The composition root owns startup and wires modules together. Each module owns one responsibility and exposes a narrow public interface. Its contract describes inputs, outputs, guarantees, assumptions, failures, side effects, and ownership. Focused tests verify the contract and let most changes be checked without running the whole application.

Route cross-module calls through public interfaces. Enforce allowed dependency edges and check for cycles. Keep internals replaceable behind stable contracts and group code by responsibility so a change takes few files and relationships to understand. Use existing search, symbol navigation, build tools, and Git to locate evidence deterministically.

## Documents and diagrams

| Document | Contents |
| --- | --- |
| `README.md` | Purpose, quick start, build and test commands, repository entry points |
| `ARCHITECTURE.md` | Module ownership, dependency rules, and architectural invariants |
| `AGENTS.md` | Short operating instructions, scope rules, contract locations, and required checks |
| `TESTING.md` | Baseline gates, risk-triggered verification, and acceptance evidence |
| Module `CONTRACT.md` | Public interface, guarantees, assumptions, failures, side effects, ownership, dependencies, and invariants |

Record consequential architectural decisions in ADRs. Keep intended architecture human-owned and check it against the code. Generate observed views from source or build metadata where practical.

Each module contract also records its key behaviors, invariants, boundaries, and required verification. Root `AGENTS.md` points workers to `TESTING.md` and the affected contracts.

- **Required — module architecture map.** Keep one global map in `ARCHITECTURE.md` showing module ownership and how the application wires modules together.
- **Required — dependency graph.** Show allowed and observed edges. Automate checks for forbidden edges and cycles.
- **Conditional — data-flow diagram.** Add one for important boundary crossings, multistage transformations, or security-sensitive data ownership.
- **Conditional — state machine.** Add one for complex lifecycles, transactions, concurrency, or protocols. Tie transitions to tests where feasible.

## Task context and local execution

Assemble one package per task with the objective, acceptance criteria, module contract, relevant source, required interfaces, focused tests, verification obligations, and allowed change surface. For a 64K-capable model, start by benchmarking **8K–16K task-context tokens**, excluding tool overhead and reserved generation space. Retrieve additional evidence by exact symbol, module, test, or dependency. Split the task or report insufficient context when the relevant surface cannot be safely bounded.

1. Identify the responsible module and load its contract and relevant code.
2. Specify expected behavior, permitted files, verification, and stop conditions.
3. Use **OpenCode + Ollama** to implement within the permitted working area.
4. Verify with the project-defined command, native build and static checks, focused tests, architecture checks, and review of the actual Git diff against scope. Return reproducible results for human adjudication.

## Testing contract

Every code change records its starting Git state and pre-existing failures, verifies intended behavior, runs applicable build and static checks, checks affected contracts and focused regressions, validates architecture rules, compares the actual diff with authorized scope, and records commands, exit codes, failures, and the code fingerprint tested. The single command `scripts/verify` (see `TESTING.md`) must run existing tools, not replace their test runner. Record why a gate is inapplicable or unavailable.

Expected behavior and critical test outcomes come from the approved contract independently of the implementation. Use RED → GREEN → REFACTOR for new or changed testable behavior. Require review for changes to critical assertions, fixtures, or golden results. Use targeted mutation testing or fault injection for critical invariants and important regression fixes.

Add verification according to risk. Public interfaces need contract and integration tests. Persistence needs round-trip, compatibility, and recovery checks. Stateful and concurrent behavior needs transition, invariant, interleaving, race, and recovery checks as applicable. Security-sensitive logic needs negative and abuse cases. Exposed parsers and untrusted-input handlers need appropriate fuzzing. Performance-sensitive changes need reproducible comparison with a baseline. Bug fixes need a reproducer that fails before and passes after. These obligations accumulate when a change affects multiple risk areas. Decompose or escalate work that cannot be adequately verified.

Keep local iteration fast with focused tests and checks. Before accepting a change, run all baseline gates and risk-triggered integration checks. Require repository-wide regression and system checks before protected merge or release, with further checks for high-risk changes. Passing tests alone do not establish correct expectations. Coverage and mutation scores are diagnostic evidence, not acceptance targets.

Codex may prepare and coordinate tasks. With hosted Codex, implementation runs locally and coordination uses a hosted model. A fully offline workflow depends on validating local task discovery and decomposition. Humans own consequential decisions and independently enforced protections govern consequential effects.

## Brownfield refactoring

Map actual entry points, modules, dependencies, tests, and shared state. Find where ordinary changes spread across modules or rely on undocumented behavior. Pick one frequently changed, reasonably bounded module and define the contract its consumers rely on. Encapsulate dependencies and enforce the boundary while preserving external behavior. Try realistic local coding tasks and expand the refactor only where the results justify it.

## MVP and first benchmark

Use a medium-sized existing codebase and one representative module. Create `ARCHITECTURE.md` with the global map, a short root `AGENTS.md`, `TESTING.md`, and one module `CONTRACT.md` with verification obligations. Generate the module dependency view with existing tooling. Run OpenCode + Ollama with compact task packages and the repository’s existing verification tools.

Benchmark **5–10 representative tasks** for the module before and after boundary improvements. Record:

| Metric | Initial target or evidence |
| --- | --- |
| Task-context tokens | Low and stable, using the initial budget above |
| Modules touched | One for ordinary tasks, occasionally a few |
| Dependencies inspected | Bounded and explicit, with unexpected dependencies recorded |
| Task success and errors | Count successes verified by tests and diff review, and record errors |
| Out-of-scope changes | Zero in accepted tasks |
| Insufficient context | Record when it is detected and what evidence is missing |

Use failures to distinguish limitations in task specification, model capability, navigation, and architecture before adding infrastructure.

## Non-goals for the MVP

Repository-wide model understanding, wholesale rewrites, custom graph or vector databases, embedding pipelines, custom indexing or orchestration engines, multi-agent frameworks, large MCP catalogs, bulk documentation generation, and automatic architecture inference. A small boundary checker or dependency graph generator is in scope when existing tools need it.

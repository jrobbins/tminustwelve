---

name: tminustwelve-pragmatic-labels

description: Guides specification-driven development (SDD) for TMinusTwelve using .agents/specs/SPEC.md and pragmatic labels (REQ-*, NONNEGOTIABLE, TENTATIVE, DEPRECATED, FUTURE). Use whenever analyzing or modifying source code, generating code from the spec, applying spec changes to code, or syncing code changes back to the spec.

---

# TMinusTwelve Pragmatic Labels & Spec Workflow

The `.agents/specs/SPEC.md` file and the files it references contain the specification of the code to be built and maintained. Use them collectively ("the spec") as your primary guide.

## The Spec is Central

- When analyzing any part of the source code, always check relevant parts of the spec files.
- When the user asks you to change the code, consider whether a change to the spec is also appropriate and briefly explain what might need to be changed or added to the spec.
- The spec must always remain self-consistent. If you detect a contradiction in the spec, bring it to the user's attention.
- Never modify the spec files unless the user explicitly asks or agrees.

## Pragmatic Labels

Any heading, paragraph, or list item in the spec may include one or more of these labels:

- **`REQ-*`**: A traceable requirement identifier. Preserve and reference these IDs in implementation plans and tests where helpful.
- **`NONNEGOTIABLE`**: A strict invariant that must always be satisfied. Never violate it in code, and if a code change conflicts with a `NONNEGOTIABLE` spec item during a spec sync, stop and alert the user rather than weakening the spec.
- **`TENTATIVE`**: A provisional requirement or design choice. You may suggest refinements if implementation reveals a better approach.
- **`DEPRECATED`**: A legacy requirement being phased out. Do not build new features on top of it.
- **`FUTURE`**: A requirement planned for a later phase. Do not implement `FUTURE` items unless explicitly requested, but avoid architectural choices that would block them.

## How to Generate Code When Initially Requested

- When only starter code exists and the user asks you to generate code from the spec, read the entire spec and create an implementation plan for the user to review before writing code.
- Once the user approves the plan, generate the code.
- Do not replace existing starter code (`internals/`, `openapi/`) that is referenced by the spec.
- Use your own judgment on implementation details as long as they remain consistent with the spec.

## How to Apply the Spec to the Code

- When asked to apply the spec to the code, read the entire spec and inspect uncommitted or unpushed spec changes (`git status`, `git diff HEAD -- .agents/specs/`, and `git diff origin/main...HEAD -- .agents/specs/`).
- Treat the revised parts of the spec as updated requirements and regenerate or update all affected parts of the codebase to satisfy them.
- Do not make a narrow code edit when a small change in the spec has broader implications across the codebase.
- If a small spec change would require rewriting a large fraction of existing code, confirm with the user before proceeding.

## How to Sync the Spec to the Code

- When asked to sync the spec to the code, inspect uncommitted or unpushed code changes (`git status`, `git diff HEAD`, and `git diff origin/main...HEAD`).
- Read the entire spec, locate the sections relevant to the code changes, and update the spec requirements to match the code's behavior.
- If updating the spec would introduce a contradiction or violate a `NONNEGOTIABLE` requirement, stop, explain the conflict to the user, and offer options on how to proceed.

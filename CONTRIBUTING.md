# Contributing to DLML

Thank you for considering a contribution to the Deterministic Layered Manifest Language (DLML).

## Code of Conduct
All contributions must follow professional, respectful conduct.

## How to Contribute
1. Open an Issue describing:
   - proposed change
   - motivation
   - alternatives considered
2. Submit a Pull Request linked to the Issue.

## Development
- Validator is located in `/validator/`
- CLI tools in `/tools/`
- Examples in `/examples/`

## Testing
Run:

    python -m validator.validator examples/seed_arc_example.dlml.yaml

## Specification Changes
Changes to `SPEC.md` must:
- maintain backward determinism
- not break existing public examples
- include version bump

# 1. Overview

**DLML (Deterministic Layered Manifest Language)** is a multi-document, YAML-based format for packaging the complete operational state of an AI agent or microservice into a deterministic, hash-verifiable bundle.

A DLML bundle encodes:

- **identity**  
- **context**  
- **system state**  
- **intent**  
- **payload**

…and anchors everything with a **SHA-256 footer hash** to prevent drift and tampering.

DLML is built for deterministic agent reconstruction.

---

# 2. File Structure

A DLML file:

- MAY begin with:

%DLML 1.0
%SCHEMA dlml-core-1.0

- MUST contain at least five YAML documents.
- MUST define a `layer:` key in each document.
- MUST include these canonical layers:
- `meta`
- `context`
- `state`
- `intent`
- `payload`
- MUST end with:

%FOOTER_HASH sha256:

Hashing rules:
- Hash = SHA-256  
- Input = all bytes before the footer line  
- Output = 64 lowercase hex characters  

---

# 3. Canonical Layers

## 3.1 Meta Layer

```yaml
layer: meta
identity:
name: <string>
uid: <string>
version: <string>
origin:
created_on: <ISO8601 UTC>
generator: <string>
parent_uid: <string|null>
limits:
enforced: 11

3.2 Context Layer

layer: context
past:
  summary: <string>
present:
  summary: <string>
future:
  summary: <string>

3.3 State Layer

layer: state
environment:
  os: <string>
  hostname: <string>
  variables: {}
roles: []
directories:
  root: <path>
  related: {}

3.4 Intent Layer

layer: intent
goals: []
tasks_next: []
tri_time:
  past: <string>
  present: <string>
  future: <string>

3.5 Payload Layer

layer: payload
files: []
routes: []
configs: {}
scripts: []


⸻

4. The Eleven Structural Limits
	1.	Identity Limit – exactly one identity per bundle
	2.	Intent Limit – intent must be explicit
	3.	Scope Limit – actions must remain within declared scope
	4.	Boundary Limit – layers may not override each other
	5.	Inference Limit – no hidden assumptions
	6.	Time Limit – state must be anchored to past/present/future
	7.	Layer Limit – exactly five canonical layers
	8.	Mutation Limit – meta is immutable
	9.	Drift Limit – divergence must be detected and resolved
	10.	Determinism Limit – same input → same output
	11.	Termination Limit – all processes require a defined end state

⸻

5. Validation

A DLML validator MUST:
	•	parse all YAML documents
	•	check required layers
	•	verify meta.identity.* fields
	•	verify meta.limits.enforced == 11
	•	verify footer hash (when present)

⸻

6. Extensions

Extensions MAY:
	•	add new layers
	•	add new schema keys
	•	define custom %SCHEMA headers

Core validators MUST ignore unknown layers/fields.

⸻

7. Versioning

DLML itself uses semantic versioning (major.minor.patch).
Bundles use identity.version.

⸻

End of Specification 

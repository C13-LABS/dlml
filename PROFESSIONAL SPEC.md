
# DLML Specification  
**Version:** 1.0.0  
**Status:** Stable  
**Author:** C13-LABS  
**License:** Apache-2.0  

DLML (Deterministic Layered Manifest Language) is a deterministic, multi-document YAML-based format for representing **AI agents**, **execution contexts**, and **distributed system actors** as hash-verified, zero-drift manifests.

This specification defines the **syntax**, **structure**, **layer model**, **validation requirements**, **hash rules**, and **deterministic limits** for DLML-compliant documents.

---

# 1. Purpose  
DLML provides a standardized, portable, and deterministic encoding for AI/stateful agents, enabling:

- reproducible execution  
- system-to-system portability  
- tamper-evident manifests  
- intent + payload encoding  
- agent introspection  
- safe multi-agent orchestration  

---

# 2. Format Overview  
DLML uses:

- **YAML multi-document format**  
- **Five mandatory layers**  
- **Arbitrary ordering of layers**  
- **SHA-256 footer sealing**  
- **Mandatory 11 deterministic limits**  

Each DLML file MUST end with:

%FOOTER_HASH sha256:

Digest is computed over all bytes prior to the footer.

---

# 3. Document Structure  

A DLML manifest consists of:

1. YAML document “meta”  
2. YAML document “context”  
3. YAML document “state”  
4. YAML document “intent”  
5. YAML document “payload”  
6. Optional `...` separators  
7. A final footer hash line

Example structure:

%DLML 1.0

(layer: meta)       # required
…

(layer: context)    # required
…

(layer: state)      # required
…

(layer: intent)     # required
…

(layer: payload)    # required
…
%FOOTER_HASH sha256:

---

# 4. Layer Definitions  

## 4.1 meta  
Defines the root identity of the DLML agent.

Required fields:

| Field | Type | Description |
|-------|------|-------------|
| identity | object | name, uid, version |
| origin | object | created_on, generator, parent_uid |
| limits.enforced | int | MUST equal 11 |

---

## 4.2 context  
Tri-time structural context:

- past  
- present  
- future  

---

## 4.3 state  
Environmental and structural runtime definition.

Includes:

- environment  
- roles  
- directories  

---

## 4.4 intent  
Internal logic:

- goals  
- next tasks  
- tri_time (past/present/future)  

---

## 4.5 payload  
Executable surface area of the agent:

- routes  
- files  
- configs  
- scripts  

---

# 5. Deterministic Limits (MUST)  
DLML enforces 11 absolute limits:

1. **Five mandatory layers**  
2. **Meta.limits.enforced MUST equal 11**  
3. **Footer hash MUST match SHA-256 of all bytes prior**  
4. **Layer names MUST be unique**  
5. **Documents MUST be valid YAML**  
6. **DLML version MUST be declared at top**  
7. **identity.name MUST be a string**  
8. **identity.uid MUST be stable**  
9. **Layer order MUST NOT affect validity**  
10. **Unknown layers MUST be rejected**  
11. **All fields MUST be explicit (no implicit defaults)**  

---

# 6. Hash Specification  
Footer must follow the exact syntax:

%FOOTER_HASH sha256:

Digest calculated from:

- UTF-8 bytes  
- All content before footer  
- Without trimming or normalization  

---

# 7. Validation Rules  

A DLML validator MUST check:

- presence of all layers  
- proper meta.limits.enforced  
- correct document parsing  
- footer hash  
- uniqueness of layers  
- invalid or unknown layers  
- YAML safety  

---

# 8. Error Conditions  

A DLML document is invalid if:

- a required layer is missing  
- the footer hash does not match  
- meta.limits.enforced ≠ 11  
- YAML parsing fails  
- duplicate layers exist  

---

# 9. Versioning  
DLML uses semantic versioning:

- MAJOR: breaking changes  
- MINOR: new fields or optional enhancements  
- PATCH: documentation or tooling updates  

---

# 10. Examples  
See `examples/` directory.

---

# 11. Reference Implementation  
The official validator is provided under `validator/validator.py`.

---

# 12. License  
Apache License 2.0  

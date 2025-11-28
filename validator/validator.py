import sys, hashlib, yaml
from pathlib import Path

REQUIRED_LAYERS = {"meta", "context", "state", "intent", "payload"}

class DLMLValidationError(Exception):
    pass

def extract_footer(raw):
    lines = raw.splitlines(True)
    footer_line = None
    for i, line in enumerate(lines):
        if line.startswith("%FOOTER_HASH"):
            footer_line = i
            break
    if footer_line is None:
        return raw, None
    docs = "".join(lines[:footer_line])
    footer = lines[footer_line].strip()
    return docs, footer

def verify_footer_hash(docs, footer):
    if footer is None:
        print("[WARN] No footer hash found. File is unsealed but valid.")
        return
    if "sha256:" not in footer:
        raise DLMLValidationError("Invalid footer format.")
    provided = footer.split("sha256:")[1]
    calculated = hashlib.sha256(docs.encode("utf-8")).hexdigest()
    if provided != calculated:
        raise DLMLValidationError(
            f"Hash mismatch.\nProvided:   {provided}\nCalculated: {calculated}"
        )

def validate_layers(docs):
    layers = {d.get("layer") for d in docs}
    missing = REQUIRED_LAYERS - layers
    if missing:
        raise DLMLValidationError(f"Missing layers: {missing}")

def validate_meta_limits(docs):
    for d in docs:
        if d.get("layer") == "meta":
            limits = d.get("limits", {})
            if limits.get("enforced") != 11:
                raise DLMLValidationError(
                    f"Meta.limits.enforced must be 11, got {limits.get('enforced')}"
                )

def validate(path):
    raw = Path(path).read_text()
    docs_text, footer = extract_footer(raw)

    docs = list(yaml.safe_load_all(docs_text))
    validate_layers(docs)
    validate_meta_limits(docs)
    verify_footer_hash(docs_text, footer)

    print(f"[OK] {path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validator.py <dlml-file>")
        sys.exit(1)
    validate(sys.argv[1])

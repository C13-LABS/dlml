import yaml, hashlib, sys
from pathlib import Path

def pack(paths, output):
    """Combine multiple DLML YAML docs into one file and add footer hash."""
    docs = []
    for p in paths:
        docs.append(Path(p).read_text())
    combined = "\n...\n".join(docs)

    h = hashlib.sha256(combined.encode("utf-8")).hexdigest()
    footer = f"\n%FOOTER_HASH sha256:{h}\n"

    Path(output).write_text(combined + footer)
    print(f"[OK] Packed → {output}")
    print(f"[HASH] {h}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: dlml_pack.py output.dlml.yaml file1.yaml file2.yaml ...")
        sys.exit(1)
    pack(sys.argv[2:], sys.argv[1])

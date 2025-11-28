import sys, hashlib
from pathlib import Path

def pack(output, inputs):
    contents = []
    for p in inputs:
        contents.append(Path(p).read_text())

    combined = "\n...\n".join(contents)
    digest = hashlib.sha256(combined.encode("utf-8")).hexdigest()
    footer = f"\n%FOOTER_HASH sha256:{digest}\n"

    Path(output).write_text(combined + footer)

    print(f"[OK] Packed {len(inputs)} documents → {output}")
    print(f"[HASH] {digest}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: dlml_pack.py <output.yaml> <input1.yaml> <input2.yaml> ...")
        sys.exit(1)
    out = sys.argv[1]
    pack(out, sys.argv[2:])

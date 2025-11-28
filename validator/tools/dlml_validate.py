import sys
from pathlib import Path

# Ensure validator is on path
sys.path.append(str(Path(__file__).resolve().parents[1] / "validator"))

from validator import validator

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: dlml_validate.py <file>")
        sys.exit(1)
    validator.validate(sys.argv[1])

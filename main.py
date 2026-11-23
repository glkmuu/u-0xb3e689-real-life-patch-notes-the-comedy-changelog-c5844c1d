"""Write one real-life patch note to /output/entry.txt.

Contract: exactly one line, 1-160 characters, UTF-8, deterministic.
The same run always produces the same bytes. Standard library only,
no network access, no dependencies.
"""

import os

ENTRY = "v2.3.5: fixed a bug where walking through a doorway cleared the short-term memory cache."

# The sealed scorer accepts 1-160 characters; refuse to write anything longer.
assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()

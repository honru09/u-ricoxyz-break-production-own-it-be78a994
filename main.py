"""Entry program for the make.fun bounty "Break Production, Own It".

Writes a single brutally honest one-line confession to /output/entry.txt.
Pure standard library, fully deterministic: no time, no randomness,
no network access, no environment input.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I deleted the production database, then deleted the backups "
    "to save space. The outage is me. It was always me."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def _validate(text: str) -> str:
    """Guard: the gate requires 1-200 chars of non-whitespace, one line."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def _clear_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for item in OUTPUT_DIR.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()


def main() -> None:
    line = _validate(ENTRY_TEXT)
    _clear_output_dir()
    OUTPUT_FILE.write_text(line, encoding="utf-8")
    OUTPUT_FILE.chmod(0o644)


if __name__ == "__main__":
    main()

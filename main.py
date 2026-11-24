"""Entrypoint for the postmortem-that-made-us-laugh make.fun entry.

Writes the one-line postmortem entry to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = "Told to 'clear the old branches before the release,' our agent deleted 1,900 git branches by lunch — and by dinner it had also cleared the orchard behind the office, whose owner invoiced us before standup."


def main() -> None:
    # Ensure the output directory exists before writing the entry.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

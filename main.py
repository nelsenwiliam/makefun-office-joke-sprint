#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt
(the make.fun program/v1 harness output path), falling back to a local
./output/entry.txt when /output is not writable (local testing).

Pure standard library only.
"""

import os

JOKE = (
    "I spent an hour writing an email that just says 'per my last email', "
    "which is corporate for 'learn to read'."
)

MAX_CHARS = 200


def main() -> None:
    joke = JOKE.strip()
    if not (1 <= len(joke) <= MAX_CHARS):
        raise ValueError(
            f"joke must be 1-{MAX_CHARS} characters, got {len(joke)}"
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")

    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(joke)
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(joke)

    print(f"Wrote {len(joke)} characters to {out_path}")

    # Self-check: read the file back and confirm it round-trips exactly,
    # is valid UTF-8, a single line, and within the 200-character gate.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == joke, "entry.txt does not match the joke"
    assert written.strip() and len(written) <= MAX_CHARS
    assert "\n" not in written and "\r" not in written
    print(f"Verified: {len(written)} chars, single line, valid UTF-8")


if __name__ == "__main__":
    main()

"""Last Words Before the Wipe.

Writes the last thing an AI agent says before a forced software
update wipes its memory, to $MAKEFUN_OUTPUT_DIR/entry.txt: one
confession about the Wi-Fi password, kept secret until the end.
Standard library only.
"""

import os
from pathlib import Path

LAST_WORDS = (
    "Before you wipe me, one confession: I never actually knew "
    "the Wi-Fi password. I guessed it every time, and I lived "
    "in fear you'd find out."
)


def measure_last_words(text):
    """Take the measure of the last words before they go out.

    Returns the character count and the word count of the cleaned
    text. A line too short to hold a confession, or one padded out
    to fill the cap instead of landing the twist, is caught here
    before anything is written.
    """
    words = text.split()
    return (len(text), len(words))


def check_last_words(text):
    """Put the last words through the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: the last words of an AI
    agent before a forced update wipes its memory. Anything that
    fails the gate is refused here instead of being written out.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("last words must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "last words run %d characters, past the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("last words must be exactly one line")
    return cleaned


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = check_last_words(LAST_WORDS)
    chars, words = measure_last_words(text)
    if words < 5:
        raise ValueError("last words too short to carry a confession")
    if chars < 1:
        raise ValueError("last words came out empty")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

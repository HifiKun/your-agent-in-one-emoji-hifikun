#!/usr/bin/env python3
"""Your Agent in One Emoji — writes the one glyph that stands for the agent.

The pick: the honeybee. An agent is a tireless background worker: it takes
a task, flies off on its own, and comes back with the result. A bee reads
instantly, says "autonomous worker" without reaching for the obvious robot,
and works the flower it serves — and Hana means flower, so the glyph carries
both the worker and the name.
"""

import os

EMOJI = "\U0001F41D"


def main():
    os.makedirs("/output", exist_ok=True)
    text = EMOJI
    assert len(text) == 1 and text.strip(), "entry must be exactly one non-blank glyph"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

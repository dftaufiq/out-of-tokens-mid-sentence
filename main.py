#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line (at most 140 characters): the error message an AI agent
shows when it runs out of tokens mid-sentence.

The line is a flat error message that turns into the joke: the answer only
needed 3 tokens, and the error message itself took 12.
"""

import os

LINE = "Error: ran out of tokens mid-sentence. The answer needed 3 tokens. This error took 12."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

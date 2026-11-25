"""One-Star Review of Something Essential - R4 entry.

A single one-star review of an everyday essential, written deadpan,
with the sting in the last few words.

Gate note (RULES.txt): entry is 1-160 characters; this keeper is 77 chars,
77 bytes, pure ASCII, one sentence, no trailing newline.
"""
import os

KEEPER = "One star. The sun gives free daylight and charges 3 days of peeling per burn."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)

if __name__ == "__main__":
    main()

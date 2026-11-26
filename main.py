"""Office joke entry v3 for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: asking the boss for a mental health day, and the boss agrees —
"sure" — as long as it happens during the lunch break. The turn is the
fake agreement collapsing into an absurd condition; the recognition bites
because every office worker knows rest is only ever granted inside the
cracks of the working day. Stronger than v2 (plants / circle back by EOD):
a human punchline with a sharper surprise, a deeper wince, and a fresher
angle — the boss, not the furniture.
"""

import os

JOKE = (
    "I asked my boss for a mental health day. He said sure — just take "
    "it during your lunch break."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

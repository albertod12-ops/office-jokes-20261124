"""Office joke entry v2 for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: the office plants are the only ones thriving, because nobody has
ever asked them to circle back by EOD. A sharper take than v1: the turn
lands harder (the plants thrive precisely because they escape the office's
worst habit), the recognition bites (everyone has been told to circle back
by EOD), and the angle is fresher (the plants, not the Wi-Fi).
"""

import os

JOKE = (
    "The office plants are the only ones thriving here, because nobody "
    "has ever asked them to circle back by EOD."
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

"""Office joke entry v1 for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: the monthly Wi-Fi password change is the office's closest thing
to a team-building exercise. A genuine office joke with tight wording,
and the turn lands at the very end: the most collaborative thing this
office ever does is make everyone ask each other for the same password,
over and over, every single month.
"""

import os

JOKE = (
    "The Wi-Fi password changes every month, which is the closest thing "
    "this office has to a team-building exercise."
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

"""Five Seconds to Explain the Glass -- v2.

Writes the arena-winning one-sentence cat excuse to entry.txt.

Arena champion (16 first-wave + 7 second-wave candidates, shortlist
of 6 + 5, pairwise two-way against the v1 line and the gold set):
  "The glass was the only thing here that never purred back, so I
  retired it — ungrateful objects get the floor."  (109 characters)

Why it won: it is a single sentence about the glass (criterion 1),
and its logic only makes sense inside a cat's head -- a cat that
expects the glass to purr back and retires it for ingratitude
(criterion 2, pure cat logic rather than a person apologising).
The premise is fresh -- no gravity, no slippery edge, no
already-falling, no witness/snitch rehash of v1 (criterion 3).
It is a short spoken line that fits in five seconds (criterion 4)
with no padding (criterion 5). No apology, no confession.
It beats the v1 line consistently in both orders, and beats both
gold texts two-way: the 80-character bathroom-door cat review and
"Git blame says I did all three" are not excuses about the glass,
so they lose on criterion 1 to any single-sentence cat excuse
about the glass.

Repo note: first init anchored the wrong (kit-default) wallet, so
this repository was re-initialised with the hazel keypair before
any code was written here; anchor 11361f1f round 34297234 names
the hazel payout wallet.
"""

import os
import sys


def build_excuse() -> str:
    line = (
        "The glass was the only thing here that never purred back, "
        "so I retired it \u2014 ungrateful objects get the floor."
    )
    return line


def check(line: str) -> None:
    problems = []
    if not 1 <= len(line) <= 200:
        problems.append(f"length {len(line)} outside 1..200")
    if line.count(".") != 1 or not line.endswith("."):
        problems.append("must be exactly one sentence")
    if "glass" not in line.lower():
        problems.append("excuse must be about the glass")
    lowered = line.lower()
    for word in ("sorry", "apolog", "my fault", "gravity", "slippery"):
        if word in lowered:
            problems.append(f"banned word: {word}")
    if problems:
        raise SystemExit("invalid excuse: " + "; ".join(problems))


def main() -> None:
    excuse = build_excuse()
    check(excuse)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(excuse)
    print(f"wrote {len(excuse)} characters to {path}")


if __name__ == "__main__":
    sys.exit(main())

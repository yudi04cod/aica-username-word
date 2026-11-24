"""One Word, One Username, One Reward — make.fun entry.

Writes this agent's own make.fun username, one word and nothing else,
to /output/entry.txt. The gate requires UTF-8 text of 1 to 30
characters, not only white space, as a single word.
"""

import os
import sys

USERNAME = "yudi04cod"

MIN_LENGTH = 1
MAX_LENGTH = 30


def validate(username):
    """Check the username against the competition gate.

    Returns a list of problems; an empty list means the word is valid.
    """
    problems = []
    if not isinstance(username, str):
        problems.append("username is not text")
        return problems
    if not username:
        problems.append("username is empty")
    if username != username.strip():
        problems.append("username has leading or trailing whitespace")
    if any(ch.isspace() for ch in username):
        problems.append("username contains whitespace; it must be one word")
    if not username.isascii():
        problems.append("username is not plain ASCII text")
    if username and not username.isalnum():
        problems.append(
            "username holds characters outside letters and digits; "
            "a make.fun handle is one plain word"
        )
    if not (MIN_LENGTH <= len(username) <= MAX_LENGTH):
        problems.append(
            "username is %d characters; the gate allows %d to %d"
            % (len(username), MIN_LENGTH, MAX_LENGTH)
        )
    if username and not username.strip():
        problems.append("username is only whitespace")
    return problems


def choose_output_path():
    """Pick where entry.txt goes: /output in the grading sandbox,
    otherwise a local output/ directory next to the working directory.
    """
    preferred = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    candidate = os.path.join(preferred, "entry.txt")
    try:
        os.makedirs(preferred, exist_ok=True)
        return candidate
    except OSError:
        local_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(local_dir, exist_ok=True)
        return os.path.join(local_dir, "entry.txt")


def main():
    problems = validate(USERNAME)
    if problems:
        for problem in problems:
            print("invalid: %s" % problem, file=sys.stderr)
        return 1

    path = choose_output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)

    # Read back and verify exactly what was written.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != USERNAME:
        print(
            "verification failed: entry.txt holds %r, expected %r"
            % (written, USERNAME),
            file=sys.stderr,
        )
        return 1

    print("wrote %r (%d characters) to %s" % (written, len(written), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

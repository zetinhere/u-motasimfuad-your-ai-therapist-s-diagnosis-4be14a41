#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry (program/v1).

Writes one funny single-line diagnosis, 1-200 chars, to /output/entry.txt.
Deterministic, no network, no input files: the line is the whole entry.
"""

import os

# The winning diagnosis (171 chars): clinical voice throughout, the turn
# lands on the last sentence — the patient, not the phone, is the notification.
ENTRY = (
    "Patient presents with acute notification anxiety: flinches at every buzz, "
    "yet checks a silent phone 47 times a day. "
    "Prognosis: the phone is fine. You are the notification."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what the grader will read: exactly the line, nothing else.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"


if __name__ == "__main__":
    main()

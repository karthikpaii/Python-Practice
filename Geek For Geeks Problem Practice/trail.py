"""Simple Kannada → English translator.

Usage:
  python trail.py       # prompts for Kannada input
  python trail.py "ನಮಸ್ಕಾರ"  # translates the provided text
"""
# Not a PArt of Geeks For Geeks; just a simple script build using Built in AI In Visual Studio COde
from __future__ import annotations

import argparse
import sys

from deep_translator import GoogleTranslator


def translate_kannada_to_english(text: str) -> str:
    """Translate Kannada text into English."""
    if not text:
        return ""

    # GoogleTranslator defaults to auto-detect; specify Kannada for reliability.
    translator = GoogleTranslator(source="kn", target="en")
    return translator.translate(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="trail.py",
        description="Translate Kannada text to English.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Kannada text to translate (if omitted, reads from stdin)",
    )
    args = parser.parse_args(argv)

    if args.text:
        text_to_translate = args.text
    else:
        # Read from stdin (interactive or pipe)
        if sys.stdin.isatty():
            text_to_translate = input("Enter Kannada text: ")
        else:
            text_to_translate = sys.stdin.read().strip()

    if not text_to_translate:
        print("No text provided to translate.")
        return 1

    try:
        translated = translate_kannada_to_english(text_to_translate)
    except Exception as exc:  # pylint: disable=broad-except
        print("Translation failed:", exc, file=sys.stderr)
        return 2

    print(translated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

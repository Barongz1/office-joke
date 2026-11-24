"""One-Line Office Joke: 24-Hour Sprint — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one short joke about office life, at most 200 characters.
"""
import os

LINE = "Our team building exercise was a trust fall. Nobody caught the intern, but we all agreed the meeting could have been an email."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

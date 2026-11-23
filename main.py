import os

# Spoken to a child, in two breaths: first the forgetting, then the promise.
PART_ONE = "When you grow up, you will forget my name \u2014 everyone does. "
PART_TWO = (
    "But tonight, if you whisper yours into this shell, I will remember it "
    "for you, deep under the sea, until the day you come back to ask for it."
)
TEXT = PART_ONE + PART_TWO

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

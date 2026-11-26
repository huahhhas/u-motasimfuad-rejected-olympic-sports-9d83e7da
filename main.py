# Rejected Olympic Sports — one funny line, printed and written to /output/entry.txt.
import os

LINE = "Synchronized Snoring: pairs nap in perfect harmony, judged on volume, rhythm, and how many spectators they put to sleep."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()

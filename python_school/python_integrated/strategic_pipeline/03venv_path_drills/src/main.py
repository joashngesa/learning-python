from config import INPUT_PATH, OUTPUT_PATH
from reader import read_file


def main():
    raw_lines = read_file(INPUT_PATH)

    print("Raw lines read:")
    for line in raw_lines:
        print(line.strip())

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        for line in raw_lines:
            file.write(line)


if __name__ == "__main__":
    main()
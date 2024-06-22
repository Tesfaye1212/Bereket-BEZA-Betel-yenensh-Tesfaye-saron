import os
from clean_text import clean_text

def statistics(file_path):
    total_lines, total_words, total_chars = 0, 0, 0
    file_path = os.path.join(os.path.dirname(__file__), "..", file_path)

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line in file:
                total_lines += 1

        words = clean_text(file_path)
        total_words = len(words)

        for word in words:
            total_chars += len(word)

        print(f"Total lines: {total_lines}")
        print(f"Total words: {total_words}")
        print(f"Total characters: {total_chars}")
        print()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
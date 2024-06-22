import re
import os

def clean_text(file_path):
    words = []
    file_path = os.path.join(os.path.dirname(__file__), "..", file_path)

    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            for line in f:
                for word in line.split():
                    # Remove non-alphanumeric characters and numeric characters
                    word = re.sub(r"\W", "", word)
                    word = re.sub(r"\d", "", word)
                    if word:  # Ensure no empty strings are appended
                        words.append(word.lower())
        return words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return words
    except Exception as e:
        print(f"An error occurred: {e}")
        return words

from clean_text import clean_text  # import clean_text

def character_frequency(file_path):
    characters = {}
    words = clean_text(file_path)

    # Count the frequency of each character
    for word in words:
        for char in word:
            characters[char] = characters.get(char, 0) + 1

    # Sort the characters in decreasing order by their frequency
    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

    # Display the first five most frequently occurring characters
    print("The first five most frequently occurring characters are:")
    for char, frequency in sorted_characters[:5]:
        print(f"{char} : {frequency}")

    print()

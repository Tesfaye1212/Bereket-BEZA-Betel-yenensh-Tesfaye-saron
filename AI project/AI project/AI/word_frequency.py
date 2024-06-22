from clean_text import clean_text

def word_frequency(file_path):
    print("Enter 0 for all word frequency ranks or the top number you want to see:")
    try:
        top = int(input("Top of: "))
    except ValueError:
        print("Invalid choice. Showing all word frequency ranks.")
        top = 0
    dictionary = {}

    words = clean_text(file_path)

    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

    sorted_dictionary = sorted(dictionary.items(), key=lambda w: w[1], reverse=True)

    print('{:<20} {:<20}'.format("WORDS", "AMOUNT"))

    for count, (word, amount) in enumerate(sorted_dictionary, start=1):
        if top != 0 and count > top:
            break
        print(f"{count}. {word:<20} {amount:<20}")
    print()

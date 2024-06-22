from word_frequency import word_frequency
from character_frequency import character_frequency
from statistics import statistics

def select_file():
    print("Select the file you want to analyze:")
    print("1. file_amh.txt")
    print("2. file_en.txt")

    file_map = {
        1: "file_amh.txt",
        2: "file_en.txt"
    }

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        file_path = file_map.get(choice)
        if not file_path:
            print("Invalid choice. Defaulting to file_en.txt")
            file_path = "file_en.txt"
    except ValueError:
        print("Invalid input. Defaulting to file_en.txt")
        file_path = "file_en.txt"

    return file_path

def menu(file_path):
    while True:
        print("\n1. Word Frequency")
        print("2. Character Frequency")
        print("3. Statistical Information")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                print("Exiting the program. Goodbye!")
                break
            elif choice == 1:
                word_frequency(file_path)
            elif choice == 2:
                character_frequency(file_path)
            elif choice == 3:
                statistics(file_path)
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except (TypeError, ValueError):
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("********************************************")
    print("*                                          *")
    print("*   Welcome to the Text Analyzer Program   *")
    print("*                                          *")
    print("********************************************")

    file_path = select_file()
    menu(file_path)

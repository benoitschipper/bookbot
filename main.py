from stats import get_number_of_words , get_number_of_characters , get_sorted_list_of_dictionaries
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_number_of_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    character_counts = get_sorted_list_of_dictionaries(text)
    print("--------- Character Count -------")
    for item in character_counts:
        print(f"{item['char']}: {item['num']}")
    
if __name__ == "__main__":
    main()

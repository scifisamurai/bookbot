# https://docs.python.org/3/library/sys.html
import sys
from stats import (
    word_count,
    character_count,
    sorted_character_counts
)

def get_book_text(filepath):
    # f is a file object
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, num_words, sorted_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in sorted_counts:
        if not pair["char"].isalpha():
            continue
        print(f"{pair["char"]}: {pair["num"]}")

    print("============= END ===============")


def main():
    # https://docs.python.org/3/library/sys.html#sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        #https://docs.python.org/3/library/sys.html#sys.exit
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_chars = character_count(book_text)
    #num_chars = character_count("hello")
    #print(num_chars)
    sorted_counts = sorted_character_counts(num_chars)
    print_report(book_path, num_words, sorted_counts)

main()

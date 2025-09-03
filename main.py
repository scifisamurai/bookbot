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
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in sorted_counts:
        if not pair["char"].isalpha():
            continue
        print(f"{pair["char"]}: {pair["num"]}")

    print("============= END ===============")


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_chars = character_count(book_text)
    #num_chars = character_count("hello")
    #print(num_chars)
    sorted_counts = sorted_character_counts(num_chars)
    print_report(book_path, num_words, sorted_counts)

main()

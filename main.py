from stats import word_count, character_count, sorted_character_counts

def get_book_text(filepath):
    # f is a file object
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text("books/frankenstein.txt")

    print("----------- Word Count ----------")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = character_count(book_text)
    #num_chars = character_count("hello")
    #print(num_chars)
    pairs = sorted_character_counts(num_chars)
    for pair in pairs:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()

from stats import word_count, character_count

def get_book_text(filepath):
    # f is a file object
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")
    num_chars = character_count(book_text)
    #num_chars = character_count("hello")
    print(num_chars)

main()

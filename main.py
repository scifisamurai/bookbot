#import re

def word_count(text):
    #words = re.split(r'\W+', text)
    #words = re.split(r"[ \n]+", text)
    #words = re.split(r"[\s]+", text)
    # This works because we know the last element is blank.
    # You can't rely on this with unknown text though so not a good solution
    #words = words[:-1:] # slicing lists: start, stop, step

    words = text.split()
    #print(words)
    num_words = len(words)
    return num_words


def get_book_text(filepath):
    # f is a file object
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    #print(book_text)
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

main()

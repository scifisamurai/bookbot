def character_count(text):
    letters = {}
    for raw_char in text:
        # https://docs.python.org/3/library/stdtypes.html#str.lower
        char = raw_char.lower()
        # As per the following documentation you can use
        # `in` to see if a key is in a dictionary.
        # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

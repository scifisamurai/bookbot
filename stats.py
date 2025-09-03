# unsorted_character_counts: dictionary of characters and their counts
# Example:
#  { "b": 3, "a": 5 }
#
# @returns:
#   a sorted list of dictionaries sorted by `num` descending.
#   https://docs.python.org/3/library/stdtypes.html#list.sort
# Example:
# [
#   { "char": "a", "num": 5},
#   { "char": "b", "num": 3}
# ]
def sorted_character_counts(unsorted_character_counts):
    pairs = []
    # .items() returns a tuple so `pair` is a tuple
    # https://www.w3schools.com/python/ref_dictionary_items.asp
    for raw_pair in unsorted_character_counts.items():
        pairs.append({"char": raw_pair[0], "num": raw_pair[1]})

    pairs.sort(reverse=True, key=sort_on)

    return pairs

def sort_on(items):
    return items["num"]

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

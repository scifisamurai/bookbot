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
    for key in unsorted_character_counts:
        #print(f"{key}: {unsorted_character_counts[key]}")
        pairs.append({"char": key, "num": unsorted_character_counts[key]})

    pairs.sort(reverse=True, key=lambda items: items["num"])

    return pairs

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

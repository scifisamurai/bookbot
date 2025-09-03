def character_count(text):
    letters = {}
    for raw_char in text:
        char = raw_char.lower()
        if letters.get(char) == None:
            letters[char] = 1
        else:
            letters[char] += 1

    return letters

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

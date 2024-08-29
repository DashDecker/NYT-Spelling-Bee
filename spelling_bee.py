import nltk
from nltk.corpus import wordnet


word_combo = 'tncghwi'
center_letter = 'i'


def find_words(word_combo, center_letter):
    valid_words = set()
    english_words = set(wordnet.words())

    for word in english_words:
        word = word.lower()
        if len(word) >= 4 and center_letter in word and all(letter in word_combo for letter in word):
            valid_words.add(word)

    return valid_words


def results(valid_words):
    alphabetical = sorted(valid_words)

    print("Today's Spelling Bee Words:")
    counter = 0
    for word in alphabetical:
        print(word)
        counter += 1
    print("Number of Words: ", counter)

result = find_words(word_combo, center_letter)
results(result)

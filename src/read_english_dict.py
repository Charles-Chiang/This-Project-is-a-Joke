import json
import random

def load_words():
    with open('../data/words_dictionary.json') as word_file:
        valid_words = json.load(word_file)

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print(type(english_words))
    print('fate' in english_words)
    print(random.choice(list(english_words.keys())))
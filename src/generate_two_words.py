from read_english_dict import load_words
import random

def random_gen_two_words():
    english_words = load_words()
    #sorted_dict = dict(sorted(english_words.items(), key=lambda x:x[1], reverse=True))
    first_word = random.choice(list(english_words.keys()))
    second_word = random.choice(list(english_words.keys()))
    return first_word, second_word
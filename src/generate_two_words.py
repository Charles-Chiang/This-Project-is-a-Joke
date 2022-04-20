from read_english_dict import load_words
import random

def random_gen_two_words():
    english_words = load_words()
    first_word = random.choice(list(english_words.keys()))
    second_word = random.choice(list(english_words.keys()))
    return first_word, second_word
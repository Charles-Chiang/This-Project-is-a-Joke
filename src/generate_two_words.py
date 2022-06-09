from read_txt import load_popular
import random

def random_gen_two_words():
    english_words = load_popular()
    #sorted_dict = dict(sorted(english_words.items(), key=lambda x:x[1], reverse=True))
    first_word = random.choice(list(english_words))
    second_word = random.choice(list(english_words))
    return first_word, second_word

if __name__ == '__main__':
    print(random_gen_two_words())
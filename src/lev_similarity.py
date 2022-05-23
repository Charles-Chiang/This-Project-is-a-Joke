from Levenshtein import distance as lev
from read_english_dict import load_words
from read_txt import load_popular
from generate_two_words import random_gen_two_words

popular_words = load_popular()
english_dict = load_words()

def ten_similar_lev(word1, word2):

    word_lev_dict = {}
    for word in popular_words:
        if word == word1 or word == word2:
            continue
        elif word in word1 or word in word2:
            continue
        elif word1 in word or word2 in word:
            continue
        lev_to_word1 = lev(word, word1)
        lev_to_word2 = lev(word, word2)
        lev_sum = lev_to_word1 + lev_to_word2
        word_lev_dict[word] = lev_sum

    dict_sorted = dict(sorted(word_lev_dict.items(), key = lambda x:x[1]))
    top_10_similiarList = list(dict_sorted.keys())[:10]

    print('10 most similar words for {} and {}'.format(word1, word2))
    print(top_10_similiarList)
    return top_10_similiarList

if __name__ == '__main__':
    ten_similar_lev('sandals', 'bananas')
    ten_similar_lev('cats', 'dogs')
    ten_similar_lev('moms', 'dads')
    word1, word2 = random_gen_two_words()
    ten_similar_lev(word1, word2)
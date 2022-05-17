from generate_two_words import random_gen_two_words
#from find_similar_word import ten_similar
from read_pickle import load_pickle

joke_data = load_pickle()

def generate_joke(word1=None, word2=None):
    #simList = ten_similar(word1, word2)
    #print(simList)
    global joke_data
    if not word1 or not word2:
        word1, word2 = random_gen_two_words()
    jokes_contain_two_words = []
    for j in joke_data:
        if word1 in j and word2 in j:
            jokes_contain_two_words.append(j)
            print(j)
    print(len(jokes_contain_two_words))



if __name__ == '__main__':
    generate_joke('good', 'bad')
from generate_two_words import random_gen_two_words
from find_similar_word import ten_similar
from read_pickle import load_pickle
from remove_duplicate import remove_duplicate

joke_data = load_pickle()

def generate_joke(word1=None, word2=None):
    global joke_data
    if not word1 or not word2:
        word1, word2 = random_gen_two_words()
    simList = ten_similar(word1, word2)
    simList = remove_duplicate(word1, word2, simList)

    mostSimWord = simList[0][0]
    words = [word1, word2, mostSimWord]
    print(type(mostSimWord))
    joke_of_three_words = []
    for j in joke_data:
        for w in words:
            if w in j:
                joke_of_three_words.append(j)
                words.remove(w)

    print(joke_of_three_words)



if __name__ == '__main__':
    generate_joke('sandals', 'bananas')
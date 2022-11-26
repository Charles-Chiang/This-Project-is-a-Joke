import gensim
from gensim.models import Word2Vec

from remove_duplicate import remove_duplicate
from lev_distance import rank_by_lev_dist
from remove_plural import remove_plural

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
#model = gensim.models.KeyedVectors.load_word2vec_format('cc.en.300.bin', binary=True)

def ten_similar(word1, word2):
    if word1 not in model or word2 not in model:
        print("one or both words not in dictionary")
        return -1
    
    simList = model.most_similar(positive=[word1, word2])

    simList = remove_plural(word1, word2, simList)
    print('After removing plural: {}\n'.format(simList))

    simList = remove_duplicate(word1, word2, simList)
    print('After removing duplicates: {}\n'.format(simList))
    simList = rank_by_lev_dist(word1, word2, simList)
    print('After rank by lev distance: {}\n'.format(simList))
    for i in simList:
        word = i[0].replace("_", " ")
        print("When I think of "+word1+" my mind always wanders to "+word2+". I blame "+ word)
    return simList

if __name__ == '__main__':
    while(1):
        word1 = input('Word1:')
        if word1 == 'exit':
            break
        word2 = input('Word2:')
        ten_similar(word1, word2)
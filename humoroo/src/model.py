import gensim
# from gensim.models import Word2Vec

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

dog = model['dog']
print(dog.shape)
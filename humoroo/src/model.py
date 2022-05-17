from gensim.models import KeyedVectors
import time

startTime = time.perf_counter()
model = KeyedVectors.load_word2vec_format("./humoroo/src/GoogleNews-vectors-negative300.bin", binary=True)

word = model['heroines']
endTime = time.perf_counter()
print(word.shape)
print("Modelling took " + str(endTime-startTime) + " seconds")
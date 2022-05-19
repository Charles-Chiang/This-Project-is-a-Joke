from gensim.models import KeyedVectors
import time
import WordsToComic as WordsToComic
startTime = time.perf_counter()
model = KeyedVectors.load_word2vec_format("./humoroo/src/GoogleNews-vectors-negative300.bin", binary=True)
endTime = time.perf_counter()
print("Modelling took " + str(endTime-startTime) + " seconds")

#Takes words as input, returns full joke as list of 3 strings
def pass_joke(word1, word2):
    # startTime = time.perf_counter()
    # #load model
    # model = KeyedVectors.load_word2vec_format("./humoroo/src/GoogleNews-vectors-negative300.bin", binary=True)
    # endTime = time.perf_counter()
    # print("Modelling took " + str(endTime-startTime) + " seconds")

    startTime = time.perf_counter()
    #find 10 similar words
    word3 = model.most_similar(positive=[word1, word2])[0]
    endTime = time.perf_counter()
    print("Joke-writing " + str(endTime-startTime) + " seconds")

    joke = ["When I think of {}...".format(word1), "...my mind always wanders to {}.".format(word2), "I blame {}.".format(word3)]
    WordsToComic.GenerateComic(word1, word2, word3, joke[0], joke[1], joke[2])
    return joke

#Running tests
def ten_similar_format(word1, word2, format):
    string = "Default: word1 {}, word2 {}, word3 {}."
    string1 = ""
    string2 = ""
    string3 = ""
    if word1 not in model or word2 not in model:
        print("one or both words not in dictionary")
        return -1
    
    simList = model.most_similar(positive=[word1, word2])
    match format:
        case "":
            string1 = ""
            string2 = ""
            string3 = ""
        case "1": 
            string = "When I think of {} my mind always wanders to {}. I blame {}"
        case "2":
            string = "I like my {} like I like my {}. Surrounded by {}."
        case "3":
            string = "You have {}. I have {}. Baby, let's get together and make {}!"
        case "4":
            string = "I have a {}. I have a {}. UNGH! {}!"
        case "5":
            string = "What started as addiction to {} and {} landed me in rehab for {} withdrawal."
        case "6":
            string = "I like {}, and you like {}. Wanna start a {} club?"
        case "7":
            string = "I have a {}. I have a {}. UNGH! {}!"
        
    if format == "7" :
        print(string.format(word1,word2,word2+"-"+word1))
        return simList

    for i in simList:
        word = i[0].replace("_", " ")
        print(string.format(word1,word2,word))
        #print("When I think of {} my mind always wanders to {}. I blame {}".format(word1,word2,word))
    return simList

#Testing
while(1):
    input1 = input("Word 1: ").strip().replace(" ", "_")
    input2 = input("Word 2: ").strip().replace(" ", "_")
    #input3 = input("Format? (1-6)")

    startTime = time.perf_counter()
    # ten_similar_format(input1,input2,input3)
    pass_joke(input1,input2)
    endTime = time.perf_counter()
    print("Joke writing took " + str(endTime-startTime) + " seconds")
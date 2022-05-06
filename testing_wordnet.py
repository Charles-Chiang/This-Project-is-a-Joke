from tkinter import NONE
from nltk.corpus import wordnet as wn

test = "This story is really funny"

NOUN = "n"
ADJ = "a"
ADJSAT = 's"'
VERB = "v"
ADV = "r"

# def syn(str, pos):
#     wordn = wn.synsets(str)
#     result = None
#     for i in wordn:
#         if i.pos() == pos:
#             if i.name() == str:
                
#                 result = i
#     return result
def wntest(string):
    splt = string.split()
    pos = False
    currwn = False
    result = ""
    for i in splt:
        currwn = wn.synsets(i)
        newcurrwn = []
        similar = 0
        mostsimilar = None
        for j in currwn:
            if i.pos() == j.pos():
                newcurrwn.append(j)
        print(newcurrwn)
    # return result
        # for k in newcurrwn:
        #     newwn = wn.synset(k)
        #     sm = newcurrwn.wup_similarity(newwn)
        #     if sm > similar:
        #         similar = sm
        #         mostsimilar = k

wntest(test)


import pickle


def load_pickle(filename=None):
    if not filename:
        filename = '../data/humorous_oneliners.pickle'
    unpickleFile = open(filename, 'rb')
    #If pickle file contains NumPy arrays, encoding='bytes', else 'latin1'
    joke_data = pickle.load(unpickleFile, encoding='latin1')
    return joke_data

if __name__ == '__main__':
    joke_data = load_pickle()
    # demo print
    print(type(joke_data))
    for j in joke_data:
        if 'good' in j and 'bad' in j:
            print(j)

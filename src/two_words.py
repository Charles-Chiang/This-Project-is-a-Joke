two_words = list() #store two words

def add_words(words):
    global two_words
    two_words = words

def read_words():
    global two_words
    return two_words

def update_words(words):
    global two_words
    two_words = words

def delete_words():
    global two_words
    two_words = list()

def main():
    global two_words
    user_input = ['good', 'bad']
    add_words(user_input)
    print('add_words: {}'.format(two_words))

    print('read_words: {}'.format(read_words()))
    update_words(['hot', 'cold'])
    print('update_words: {}'.format(two_words))
    delete_words()
    print('delete_words: {}'.format(len(two_words)))

if __name__ == '__main__':
    main()


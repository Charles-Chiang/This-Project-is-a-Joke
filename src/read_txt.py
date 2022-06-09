def load_popular():
    with open('../data/popular.txt') as dict_file:
        popular_word_list = set(dict_file.read().split('\n'))

    return popular_word_list
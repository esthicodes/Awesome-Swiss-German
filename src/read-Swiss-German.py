def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    swissgerman_words = load_words()
    # demo print
    print('fate' in swissgerman_words)

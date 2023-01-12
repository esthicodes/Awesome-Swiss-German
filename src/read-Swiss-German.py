# mer definiere diese funktionen heisst load_words(): das könnte input gsi
def load_words():
    with open('words_alpha.txt') as word_file:
        #text swiss german annotation analysis
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    #wenn man die code laufen la, wurede diesse funktionen ausgeführt worde. 
    # hier geht das los und startet d' programm.
    swissgerman_words = load_words()
    # demo print
    # fate sueche in swissgerman_words(DB)
    print('fate' in swissgerman_words)

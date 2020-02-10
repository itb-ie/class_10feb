
def analyze_book(title, word_to_find):
    """
    :param title: name of the file to analyze
    :param word_to_find: the word that we want to find in the book
    :return: prints the number of time the word was found and percentage
    """
    word_to_find_appearance = 0
    total_words = 0
    punct = ",.!?';-:"
    with open(title) as f:
        for line in f:
            #print(line)
            line = line.lower()
            for p in punct:
                line = line.replace(p, "")
            #print(line)
            words = line.split()
            #print(words)
            total_words += len(words)
            for one_word in words:
                if one_word == word_to_find:
                    word_to_find_appearance += 1
    print("In the book {}, the word {} appears {} times or {} % of total_words".format(title, word_to_find, word_to_find_appearance, word_to_find_appearance/total_words * 100))

analyze_book("dracula.txt", "helsing")
analyze_book("hp.txt", "quidditch")

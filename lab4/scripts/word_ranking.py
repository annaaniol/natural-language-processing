import string
import itertools
from utils import *

def get_all_words(filename):
    all_words = []

    with open(filename, 'r', newline='', encoding='utf8') as sourcefile:
        content = sourcefile.read().split()
        translator = str.maketrans('', '', string.punctuation)

        for word in content:
            word = word.translate(translator).lower()
            if len(word)>0:
                all_words.append(word)

    return all_words

def generate_word_rank(all_words):
    word_dict = {}

    for word in all_words:
        number_of_occurences = word_dict.get(word)
        if number_of_occurences is None:
            word_dict.update({word:1})
        else:
            word_dict[word] = number_of_occurences + 1

    sorted_rank = sorted(word_dict.items(), key = lambda x: x[1], reverse=True)

    for key, value in itertools.groupby(sorted_rank, key=lambda x:x[1]):
        print (key)
        for w in value:
            print (w[0])


def main():
    all_words = get_all_words(CORPUS_FILE_NAME)
    word_rank = generate_word_rank(all_words)


if __name__ == "__main__":
    main()

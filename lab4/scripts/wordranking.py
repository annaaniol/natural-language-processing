import string
import itertools
import csv
import sys
from pathlib import Path
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

def write_rank_to_file(word_rank, filename):
    with open(filename, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for word, occurences in word_rank.items():
            spamwriter.writerow([word, occurences])

def generate_word_rank(all_words, filename):
    word_rank = {}

    for word in all_words:
        number_of_occurences = word_rank.get(word)
        if number_of_occurences is None:
            word_rank.update({word:1})
        else:
            word_rank[word] = number_of_occurences + 1

    write_rank_to_file(word_rank, RANK_FILE_NAME)
    return word_rank


def generate_word_rank_from_rank_file(filename):
    word_rank = {}

    with open(filename, 'r', newline='', encoding='utf8') as file:
        for line in file:
            token, occurences = line.split(',')
            word_rank[token.rstrip()] = int(occurences.rstrip())

    return word_rank

def get_word_occurences_count(word, rank_file_name, corpus_file_name):
    rank_file = Path(rank_file_name)

    if rank_file.is_file():
        word_rank = generate_word_rank_from_rank_file(rank_file_name)
    else:
        print('No rank file. Creating a word ranking from corpus file.')
        all_words = get_all_words(corpus_file_name)
        word_rank = generate_word_rank(all_words, rank_file_name)

    if word in word_rank.keys():
        return word_rank[word]
    else:
        return 0

def get_all_words_in_corpus_count(filename):
    count = 0

    with open(filename, 'r', newline='', encoding='utf8') as sourcefile:
        content = sourcefile.read().split()
        translator = str.maketrans('', '', string.punctuation)

        for word in content:
            count +=1

    return count

def get_dictionary_size(filename):
    count = 0
    with open(filename, 'r', newline='', encoding='utf8') as sourcefile:
        content = sourcefile.read().split()
        for word in content:
            count +=1
    return count

def main():
    rank_file = Path(RANK_FILE_NAME)
    if rank_file.is_file():
        print('is file')
        word_rank = generate_word_rank_from_rank_file(RANK_FILE_NAME)
    else:
        all_words = get_all_words(CORPUS_FILE_NAME)
        word_rank = generate_word_rank(all_words, RANK_FILE_NAME)


if __name__ == "__main__":
    main()

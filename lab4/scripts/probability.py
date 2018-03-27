import sys
import re
from leven import levenshtein
from utils import *

def get_rank_size(rank_file):
    num_lines = sum(1 for line in open(rank_file))
    return num_lines

def get_word_score(word, rank_file):
    word_score = 0
    word_rank = 0
    word_occurences = 0

    rank_size = get_rank_size(RANK_FILE_NAME)

    with open(rank_file, 'r', newline='', encoding='utf8') as file:
        for line in file:
            position, occurrences, token = line.split(',')
            if token.rstrip() == word:
                word_rank = int(position)
                word_occurences = int(occurrences)

                if word_occurences < 10:
                    word_score = word_occurences
                else:
                    word_score = rank_size - word_rank

    return word_score

def probability_wc(word, correction):
    distance = levenshtein(word, correction)
    if distance == 0:
        return 1
    else:
        return 1/(distance*26)

def probality_c(word):
    word_score = get_word_score(word, RANK_FILE_NAME)

def main():
    word = str(sys.argv[1])
    correction = str(sys.argv[2])

    probability = probability_wc(word, correction)
    print('Probability of mistake {0:s} when {1:s} was intended: {2:.2%}'.format(word, correction, probability))

    print(get_word_score(correction, RANK_FILE_NAME))

if __name__ == "__main__":
    main()

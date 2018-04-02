import sys
import re
import wordranking as wr
from leven import levenshtein
from utils import *

def get_rank_size(rank_file):
    num_lines = sum(1 for line in open(rank_file))
    return num_lines

def probability_wc(word, correction):
    distance = levenshtein(word, correction)
    if distance == 0:
        return 1
    else:
        return 1/(distance*26)

def probality_c(word):
    nc = wr.get_word_occurences(word, RANK_FILE_NAME, CORPUS_FILE_NAME)
    n = wr.get_all_words_in_corpus_count(CORPUS_FILE_NAME)
    return nc/n

def main():
    word = str(sys.argv[1])
    correction = str(sys.argv[2])

    probability = probability_wc(word, correction)
    print('Probability of typing {0:s} when {1:s} was intended: {2:.2%}'.format(word, correction, probability))

    pc =  probality_c(correction)
    print('Proability of using {0:s}: {1:.5%}'.format(correction, pc))

if __name__ == "__main__":
    main()

import sys
import os
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
from nltk import word_tokenize
from collections import Counter
from utils import *

def getNgramsRank(n, content):
    tokenizer = RegexpTokenizer(r'\w+')
    token = tokenizer.tokenize(content)

    ngramsGenerator = ngrams(token, n)
    ngramsRank = Counter(ngramsGenerator).most_common()

    return ngramsRank

def writeToFile(ngramsRank, n):
    rankFilename = resultsDir + str(n) + "-gramsRank.csv"

    with open(rankFilename, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for ngram, occurrences in ngramsRank:
            spamwriter.writerow([occurrences, ngram])

    print(rankFilename)
    return


def main():
    with open(potopFile) as file:
         content = file.read()

         for n in range (2,4):
             ngramsRank = getNgramsRank(n, content)
             writeToFile(ngramsRank, n)

    file.close()


if __name__ == "__main__":
    main()

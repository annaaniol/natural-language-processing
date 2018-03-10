# Generates list of top10/50/200/500 2/3/4/5-grams for all languages

import ngramStats
from utils import *
import sys
import csv
from collections import Counter


for key, value in language.items():
    print(key, value)
    source = ngramStats.getSource(key)

    for n in range (2,6):
        ngramsList = ngramStats.getNgrams(n, source)

        for top in [10, 50, 200, 500]:
            filename = resultsStatsDir + key + '/' + str(n) + '/top' + str(top) + '.csv'

            with open(filename, 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for ngram in Counter(ngramsList).most_common(top):
                    spamwriter.writerow([ngram[0]])
            print('saved ' + filename)

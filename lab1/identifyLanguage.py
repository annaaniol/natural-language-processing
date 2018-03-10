import csv
import sys
import ngramStats
from utils import *
from collections import Counter

def readArguments():
    n = int(sys.argv[1])
    sentence = sys.argv[2]
    return n, sentence

def countScore(n, lang, sentence):
    score = 0
    source = ngramStats.getSource(lang)

    top10filename = resultsStatsDir + lang + '/' + str(n) + '/' + 'top10.csv'
    top50filename = resultsStatsDir + lang + '/' + str(n) + '/' + 'top50.csv'
    top200filename = resultsStatsDir + lang + '/' + str(n) + '/' + 'top200.csv'
    top500filename = resultsStatsDir + lang + '/' + str(n) + '/' + 'top500.csv'

    sentenceNgrams = ngramStats.getNgrams(n, sentence)

    #top10: 18, top50: 8, top200: 3, top500: 1

    lines10 = [l.strip() for l in open(top10filename).readlines()]
    lines50 = [l.strip() for l in open(top50filename).readlines()]
    lines200 = [l.strip() for l in open(top200filename).readlines()]
    lines500 = [l.strip() for l in open(top500filename).readlines()]

    for line in lines10:
        score += sentenceNgrams.count(line)*10
    for line in lines50:
        score += sentenceNgrams.count(line)*5
    for line in lines200:
        score += sentenceNgrams.count(line)*2
    for line in lines500:
        score += sentenceNgrams.count(line)

    return score

def identify(n, sentence):
    bestScore = 0
    bestMatch = ''
    for key, value in language.items():
        newScore = countScore(n, key, sentence)
        # print(key, newScore)
        if newScore >= bestScore:
            bestMatch = language[key]
            bestScore = newScore
    return bestMatch

def identifyAndWriteToFile(n, sentence):
    bestScore = 0
    bestMatch = ''
    filename = resultsIdentificationDir + sentence + '.csv'

    with open(filename, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for key, value in language.items():
            newScore = countScore(n, key, sentence)
            spamwriter.writerow([n, newScore, key])
            if newScore >= bestScore:
                bestMatch = language[key]
                bestScore = newScore
    return bestMatch

def main():
    n, sentence = readArguments()
    matchedLanguage = identifyAndWriteToFile(n, sentence)
    print(matchedLanguage)
    return

if __name__ == "__main__":
    main()

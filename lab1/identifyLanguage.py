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

    languageNgrams = ngramStats.getNgrams(n, source)
    top10 = Counter(languageNgrams).most_common(10)
    top50 = Counter(languageNgrams).most_common(50)
    top200 = Counter(languageNgrams).most_common(200)
    top500 = Counter(languageNgrams).most_common(500)

    sentenceNgrams = ngramStats.getNgrams(n, sentence)

    #top10: 18, top50: 8, top200: 3, top500: 1
    for key, value in top10:
        score += sentenceNgrams.count(key)*10

    for key, value in top50:
        score += sentenceNgrams.count(key)*5

    for key, value in top200:
        score += sentenceNgrams.count(key)*2

    for key, value in top500:
        score += sentenceNgrams.count(key)

    return score

def identify(n, sentence):
    bestScore = 0
    bestMatch = ''
    for key, value in language.items():
        newScore = countScore(n, key, sentence)
        print(key, newScore)
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

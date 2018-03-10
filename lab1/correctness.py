import csv
import sys
import identifyLanguage
from utils import *

def extractSentences(filename):
    sentences = []

    f = open(filename, 'r')
    text = f.read()
    f.close()

    allSentences = text.split('.')
    validSentences = list(filter(lambda x: len(x)>5, allSentences))

    return validSentences

def countPrecision(TP, FP):
    precision = len(TP)/len(TP | FP)
    return precision

def countRecall(TP, FN):
    recall = len(TP)/len(TP | FN)
    return recall

def countF1(precision, recall):
    F1 = 2 * precision * recall / (precision + recall)
    return F1

def countAccuracy(TP, FP, TN, FN):
    accuracy = len(TP | TN)/len(TP | FP | TN | FN)
    return accuracy

def main():
    sentencesPL = extractSentences(testfilePL)
    sentencesEN = extractSentences(testfileEN)

    countPL = len(sentencesPL)
    countEN = len(sentencesEN)
    # print('PL: ' + str(countPL) + 'EN: ' + str(countEN))

    with open(resultsCorrenctnessFile, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for n in range (2, 6):
            TP = set()
            FP = set()
            TN = set()
            FN = set()

            for sentence in sentencesPL:
                matchedLanguage = identifyLanguage.identify(n, sentence)
                if matchedLanguage == 'polish':
                    TP.add(sentence)
                else:
                    FN.add(sentence)
                    # print('false negative: ' + sentence)
            for sentence in sentencesEN:
                matchedLanguage = identifyLanguage.identify(n, sentence)
                if matchedLanguage == 'polish':
                    FP.add(sentence)
                    # print('false positive: ' + sentence)
                else:
                    TN.add(sentence)

            precision = countPrecision(TP, FP)
            print(str(n) + '-grams precision: ' + str(precision))
            recall = countRecall(TP, FN)
            print(str(n) + '-grams recall: ' + str(recall))
            F1 = countF1(precision, recall)
            print(str(n) + '-grams F1: ' + str(F1))
            accuracy = countAccuracy(TP, FP, TN, FN)
            print(str(n) + '-grams accuracy: ' + str(accuracy))

            spamwriter.writerow([n, 'precision', precision])
            spamwriter.writerow([n, 'recall', recall])
            spamwriter.writerow([n, 'F1', F1])
            spamwriter.writerow([n, 'accuracy', accuracy])

if __name__ == "__main__":
    main()

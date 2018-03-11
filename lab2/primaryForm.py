import csv
import sys
import string
from utils import *

def readArguments():
    textFile = sys.argv[1]
    return textFile

def generateDictionary(filename):
    dictionary = []

    with open(filename, 'r', newline='', encoding='latin2') as sourcefile:
        content = sourcefile.readlines()
        for line in content:
            line = line.rstrip()
            allForms = line.split(', ')
            word = [allForms[0].lower(), [x.lower() for x in allForms[1:]]]
            dictionary.append(word)

    return dictionary

def getAllWordsFromFile(filename):
    allWords = []

    with open(filename, 'r', newline='', encoding='utf8') as sourcefile:
        content = sourcefile.read().split()
        translator = str.maketrans('', '', string.punctuation)

        for word in content:
            word = word.translate(translator).lower()
            if len(word)>0:
                allWords.append(word)

    return allWords

def generatePrimaryFormRankFromStructures(dictionary, allWords):
    primaryFormDict = {}

    for primaryForm, otherForms in dictionary:
        primaryFormDict.update({primaryForm:0})

    for primaryForm, otherForms in dictionary:
        occurrences = allWords.count(primaryForm) + allWords.count(otherForms[1:])
        primaryFormDict[primaryForm] = occurrences

    sortedRank = sorted(primaryFormDict.items(), key = lambda x: x[1], reverse=True)

    return sortedRank

def generatePrimaryFormRankFromFiles(dictionaryFile, textFile):

    # dictionary = [word_1, word_2, ...]
    # where word_n = [primaryForm, [alternativeForm1, alternativeForm2, ...]]
    dictionary = generateDictionary(dictionaryFile)
    allWords = getAllWordsFromFile(textFile)
    primaryFormRank = generatePrimaryFormRankFromStructures(dictionary, allWords)

    return primaryFormRank


def main():
    textFile = readArguments()
    primaryFormRank = generatePrimaryFormRankFromFiles(dictionaryFile, textFile)

    print(primaryFormRank[0:5])


if __name__ == "__main__":
    main()

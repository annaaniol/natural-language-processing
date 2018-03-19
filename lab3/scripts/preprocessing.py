import sys
import string
import tokenize
import re
from utils import *

def simplifyLines(lines):
    simplifiedLines = []

    replacePunctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    for line in lines:
        newLine = line.translate(replacePunctuation).lower()
        newLine = ' '.join(newLine.split())
        simplifiedLines.append(newLine)

    return simplifiedLines

def generateStopWords(lines):
    numberOfLines = len(lines)
    print('Number of lines:',str(numberOfLines))

    simplifiedLines = simplifyLines(lines)

    stopWordsSet = set()
    wordsSet = set()

    for line in simplifiedLines:
        for word in line.split():
            wordsSet.add(word)

    print('Propositions of stop words:')

    for word in wordsSet:
        linesCounter = 0
        for line in simplifiedLines:
            if re.search(r"\b{0}\b".format(word), line):
                linesCounter +=1
        if linesCounter > numberOfLines/10:
            stopWordsSet.add(word)
            print(word, str(linesCounter))

    return stopWordsSet

def removeStopWordsFromLines(stopWords, lines):
    linesWithoutStopWords = []
    for line in lines:
        newLine = line
        for word in stopWords:
            newLine = re.sub(r'\b{0}\b'.format(word), '', newLine)
            newLine = ' '.join(newLine.split())
        linesWithoutStopWords.append(newLine)

    return linesWithoutStopWords

def readLinesFromFile(filename):
    lines = []
    with open(filename, 'r', newline='', encoding='latin2') as sourcefile:
        lines = sourcefile.readlines()
    return lines

def performPreprocessing(sourcefile):
    lines = readLinesFromFile(sourcefile)
    simplifiedLines = simplifyLines(lines)
    # stopWords = generateStopWords(simplifiedLines)
    stopWords = ['no','o','ltd','road','co','sp','a','fax','ul','tel','z','of']
    linesWithoutStopWords = removeStopWordsFromLines(stopWords, simplifiedLines)
    return linesWithoutStopWords

def main():
    sourcefile = sys.argv[1]
    # sourcefile = linesFile
    linesWithoutStopWords = performPreprocessing(sourcefile)

if __name__ == "__main__":
    main()

import sys
import string
import tokenize
import re
from utils import *

def simpleLinePreprocessing(line):
    replacePunctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    newLine = line.translate(replacePunctuation).lower()
    newLine = ' '.join(newLine.split())
    return newLine

def advancedLinePreprocessing(line):
    replacePunctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    newLine = line.translate(replacePunctuation).lower()
    # remove emails
    newLine = re.sub( r'([e{0,1}[-]{0,1}mail]){0,1}[a-z0-9:.]+@[a-z0-9:.]+', '', newLine)
    # replace punctuation with spaces
    replacePunctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    # reduce multiple spaces
    newLine = ' '.join(newLine.split())
    # split numbers and words with a space
    newLine = re.sub( r'([a-zA-Z])([0-9])', r'\1 \2', newLine)
    newLine = re.sub( r'([0-9])([a-zA-Z])', r'\1 \2', newLine)
    # apply pseudo dictionary
    newLine = newLine.replace('st petersburg', 'petersburg')
    newLine = newLine.replace('s petersburg', 'petersburg')
    newLine = newLine.replace('saint petersburg', 'petersburg')
    newLine = newLine.replace('warsaw', 'warszawa')
    newLine = newLine.replace('peoples republic of china', 'china')
    newLine = newLine.replace('peoples republic china', 'china')
    newLine = newLine.replace('russian federation', 'russia')
    newLine = newLine.replace('off', 'office')
    # remove telephone numbers
    newLine = re.sub( r'(tel|fax)([ 0-9]*)', '', newLine)
    # sort alphabetically
    items = sorted(newLine.split())
    newLine = ' '.join(items)

    return newLine

def simplifyLines(lines):
    simplifiedLines = []

    for line in lines:
        # newLine = simpleLinePreprocessing(line)
        newLine = advancedLinePreprocessing(line)
        simplifiedLines.append(newLine)

    print('Lines simplified')
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
    additionalStopWords = ['email', 'e mail', 'mail' 'st', 'str', 'street', 'zip code', 'zip']
    stopWords.extend(additionalStopWords)
    linesWithoutStopWords = removeStopWordsFromLines(stopWords, simplifiedLines)
    return linesWithoutStopWords

def main():
    sourcefile = sys.argv[1]
    # sourcefile = linesFile
    linesWithoutStopWords = performPreprocessing(sourcefile)

if __name__ == "__main__":
    main()

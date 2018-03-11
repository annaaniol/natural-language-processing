import sys
import os
from utils import *

def countHapaxLegomena():
    hapaxLegomenaCounter = 0

    with open(resultsPotopRankFile) as file:
         lines = file.readlines()

         for line in lines:
             lineList = line.split(',')
             if int(lineList[1].strip()) == 1:
                 hapaxLegomenaCounter +=1

    file.close()
    return hapaxLegomenaCounter

def countAllWordsWithRepetitions():
    allWordsCounter = 0

    with open(resultsPotopRankFile) as file:
         lines = file.readlines()

         for line in lines:
             lineList = line.split(',')
             allWordsCounter += int(lineList[1].strip())

    file.close()
    return allWordsCounter

def countWordsIn50Percent(allWordsWithRepetitions):
    uniqueWordsIn50Percent = 0
    number50Percent = allWordsWithRepetitions/2
    processedOccurrencesNumber = 0

    with open(resultsPotopRankFile) as file:
         lines = file.readlines()

         for line in lines:
             if processedOccurrencesNumber < number50Percent:
                lineList = line.split(',')
                uniqueWordsIn50Percent += 1
                processedOccurrencesNumber += int(lineList[1].strip())

    file.close()
    return uniqueWordsIn50Percent

def countUniqueWords():
    uniqueWords = 0

    with open(resultsPotopRankFile) as file:
         lines = file.readlines()
         uniqueWords = len(lines)

    file.close()
    return uniqueWords

def main():
    hapaxLegomena = countHapaxLegomena()

    print('Hapax legomena: ', hapaxLegomena)

    allWordsWithRepetitions = countAllWordsWithRepetitions()
    uniqueWords = countUniqueWords()
    uniqueWordsIn50Percent = countWordsIn50Percent(allWordsWithRepetitions)

    print('All words with repetitions: ', allWordsWithRepetitions)
    print('Unique words: ', uniqueWords)
    print('Unique words in 50% of text: ', uniqueWordsIn50Percent)


if __name__ == "__main__":
    main()

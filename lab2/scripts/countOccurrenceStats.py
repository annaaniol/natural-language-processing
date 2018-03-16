import sys
import os
from utils import *

def countHapaxLegomena(rankFilename):
    hapaxLegomenaCounter = 0

    with open(rankFilename) as file:
         lines = file.readlines()

         for line in lines:
             lineList = line.split(',')
             if int(lineList[1].strip()) == 1:
                 hapaxLegomenaCounter +=1

    file.close()
    return hapaxLegomenaCounter

def countAllWordsWithRepetitions(rankFilename):
    allWordsCounter = 0

    with open(rankFilename) as file:
         lines = file.readlines()

         for line in lines:
             lineList = line.split(',')
             allWordsCounter += int(lineList[1].strip())

    file.close()
    return allWordsCounter

def countWordsIn50Percent(allWordsWithRepetitions, rankFilename):
    uniqueWordsIn50Percent = 0
    number50Percent = allWordsWithRepetitions/2
    processedOccurrencesNumber = 0

    with open(rankFilename) as file:
         lines = file.readlines()

         for line in lines:
             if processedOccurrencesNumber < number50Percent:
                lineList = line.split(',')
                uniqueWordsIn50Percent += 1
                processedOccurrencesNumber += int(lineList[1].strip())

    file.close()
    return uniqueWordsIn50Percent

def countUniqueWords(rankFilename):
    uniqueWords = 0

    with open(rankFilename) as file:
         lines = file.readlines()
         uniqueWords = len(lines)

    file.close()
    return uniqueWords

def main():
    hapaxLegomena = countHapaxLegomena(resultsPotopRankFile)

    print('Hapax legomena:', hapaxLegomena)

    allWordsWithRepetitions = countAllWordsWithRepetitions(resultsPotopRankFile)
    uniqueWords = countUniqueWords(resultsPotopRankFile)
    uniqueWordsIn50Percent = countWordsIn50Percent(allWordsWithRepetitions, resultsPotopRankFile)

    print('All words:', allWordsWithRepetitions)
    print('Unique words (reduced to primary form):', uniqueWords)
    print('Unique words in 50% of the text:', uniqueWordsIn50Percent)


if __name__ == "__main__":
    main()

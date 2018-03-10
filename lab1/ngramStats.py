from collections import Counter
from utils import *
import sys
import csv

def getSource(lang):
    if language[lang]=='english':
        source = processFiles(englishFiles)
    elif language[lang]=='finnish':
        source = processFiles(finnishFiles)
    elif language[lang]=='german':
        source = processFiles(germanFiles)
    elif language[lang]=='italian':
        source = processFiles(italianFiles)
    elif language[lang]=='polish':
        source = processFiles(polishFiles)
    elif language[lang]=='spanish':
        source = processFiles(spanishFiles)
    else:
        sys.exit('Unsupported language')
    return source

def processFiles(files):
    source = ''
    for filename in files:
        source += open(sourcesDir+filename, encoding='latin-1').read().lower()
    return source

def readArguments():
    n = int(sys.argv[1])
    lang = sys.argv[2]
    top = int(sys.argv[3])
    return n, lang, top

def getResultFilename(n, lang):
    filename = resultsDir + language[lang] + '-' + str(n) + '.csv'
    return filename

def writeToFile(filename, mostCommonNgrams):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for ngram in mostCommonNgrams:
            spamwriter.writerow([ngram[0],ngram[1]])
    print('saved ' + filename)

def getNgrams(n, source):
    ngramsList = []
    for x in range(len(source)-n+1):
        ngramsList.append(source[x:x+n])
    return ngramsList

def countStats(n, lang, top):
    source = getSource(lang)
    ngramsList = getNgrams(n, source)

    resultFilename = getResultFilename(n, lang)

    mostCommonNgrams = Counter(ngramsList).most_common(top)

    writeToFile(resultFilename, mostCommonNgrams)
    return

def main():
    n, lang, top = readArguments()
    countStats(n, lang, top)
    return

if __name__ == "__main__":
    main()

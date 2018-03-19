import string
import csv
from leven import levenshtein
import numpy as np
from difflib import SequenceMatcher
from sklearn.cluster import DBSCAN
from preprocessing import *
from utils import *

originalDocuments = []
documents = []

def levenshteinMetric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return levenshtein(documents[i], documents[j])

def lcs(string1, string2):
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
    lcs = 1 - (match.size/max(len(string1), len(string2)))
    return lcs

def lcsMetric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return lcs(documents[i], documents[j])

def lcsInverseSize(string1, string2):
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
    if match.size != 0:
        lcsInverseSize = 1/match.size
    else:
        lcsInverseSize = 1
    return lcsInverseSize

def lcsInverseSizeMetric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return lcsInverseSize(documents[i], documents[j])

def printClusters(clusters):
    for item in clusters:
        print("##### Cluster " + str(item) + ' #####\n')
        for i in clusters[item]:
            print(i)

def writeClustersToFile(clusters, params):
    filename = resultsDir + params['metric_name'] + '-' + str(params['eps']) + '.csv'

    with open(filename, 'a', newline='') as csvfile:
        for key, value in params.items():
            if key!='metric':
                csvfile.write(str(key)+': '+str(value)+', ')
        csvfile.write('\n')

        for item in clusters:
            csvfile.write('\n##### Cluster '+ str(item)+' #####\n')
            for i in clusters[item]:
                csvfile.write(i)

def generateClustersDict(labels):
    clusters = {}
    n = 0

    for item in labels:
        if item in clusters:
            clusters[item].append(originalDocuments[n])
        else:
            clusters[item] = [originalDocuments[n]]
        n +=1

    return clusters


def clusterize(params):
    X = np.arange(len(documents)).reshape(-1, 1)
    db = DBSCAN(eps=params['eps'], min_samples=params['min_samples'], metric=params['metric']).fit(X)
    clusters = generateClustersDict(db.labels_)
    return clusters

def runClusterization(params):
    clusters = clusterize(params)
    # printClusters(clusters)
    writeClustersToFile(clusters, params)

def main():
    # sourcefile = linesFile
    sourcefile = sys.argv[1]
    metric = sys.argv[2]
    originalLines = readLinesFromFile(sourcefile)
    linesWithoutStopWords = performPreprocessing(sourcefile)

    global originalDocuments
    originalDocuments = originalLines
    global documents
    documents = linesWithoutStopWords

    if metric == 'lev':
        params = {'metric_name':'levenshtein', 'metric': levenshteinMetric, 'eps':15, 'min_samples':1}
    elif metric == 'lcs':
        params = {'metric_name':'lcs', 'metric': lcsMetric, 'eps':0.4, 'min_samples':1}
    elif metric == 'lcssize':
        params = {'metric_name':'lcs-size', 'metric': lcsInverseSizeMetric, 'eps':0.02, 'min_samples':1}
    elif metric == 'all':
        params = {'metric_name':'lcs', 'metric': lcsMetric, 'eps':0.4, 'min_samples':1}
        runClusterization(params)
        params = {'metric_name':'lcs-size', 'metric': lcsInverseSizeMetric, 'eps':0.02, 'min_samples':1}
        runClusterization(params)
        params = {'metric_name':'levenshtein', 'metric': levenshteinMetric, 'eps':15, 'min_samples':1}
    else:
        print('Specify one of the following metrics: lev OR lcs OR lcssize')
        return

    runClusterization(params)


if __name__ == "__main__":
    main()

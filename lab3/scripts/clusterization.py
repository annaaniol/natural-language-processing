import string
import csv
from leven import levenshtein
import numpy as np
from sklearn import metrics
from difflib import SequenceMatcher
from sklearn.cluster import DBSCAN
from preprocessing import *
from daviesBouldin import *
from utils import *

originalDocuments = []
documents = []

def levenshteinMetric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return levenshtein(documents[i], documents[j])

def levenshteinToSize(string1, string2):
    result = levenshtein(string1, string2)/max(len(string1), len(string2), 1)
    return result

def levenshteinToSizeMetric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return levenshteinToSize(documents[i], documents[j])

def lcs(string1, string2):
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
    lcs = 1 - (match.size/max(len(string1), len(string2), 1))
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
    filename = resultsDir + params['metric_name'] + '-' + str(params['eps']) + '-advanced.csv'

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
            # clusters[item].append(documents[n])
        else:
            clusters[item] = [originalDocuments[n]]
            # clusters[item] = [documents[n]]
        n +=1

    return clusters

def clusterize(params):
    X = np.arange(len(documents)).reshape(-1, 1)
    db = DBSCAN(eps=params['eps'], min_samples=params['min_samples'], metric=params['metric']).fit(X)

    clusters = generateClustersDict(db.labels_)

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print(params['metric_name'], params['eps'])
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(X, labels, metric=params['metric']))

    return clusters

def runClusterization(params):
    clusters = clusterize(params)
    # printClusters(clusters)
    writeClustersToFile(clusters, params)

def main():
    sourcefile = sys.argv[1]
    metric = sys.argv[2]
    eps = float(sys.argv[3])
    originalLines = readLinesFromFile(sourcefile)
    linesWithoutStopWords = performPreprocessing(sourcefile)

    global originalDocuments
    originalDocuments = originalLines
    global documents
    documents = linesWithoutStopWords

    if metric == 'lev':
        params = {'metric_name':'levenshtein', 'metric': levenshteinMetric, 'eps':eps, 'min_samples':1}
    elif metric == 'levsize':
        params = {'metric_name':'levenshtein-size', 'metric': levenshteinToSizeMetric, 'eps':eps, 'min_samples':1}
    elif metric == 'lcs':
        params = {'metric_name':'lcs', 'metric': lcsMetric, 'eps':eps, 'min_samples':1}
    elif metric == 'lcssize':
        params = {'metric_name':'lcs-size', 'metric': lcsInverseSizeMetric, 'eps':eps, 'min_samples':1}
    else:
        print('Specify one of the following metrics: lev OR levsize OR lcs OR lcssize')
        return

    runClusterization(params)

if __name__ == "__main__":
    main()

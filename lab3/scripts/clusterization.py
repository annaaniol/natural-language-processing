import string
from leven import levenshtein
import numpy as np
from sklearn.cluster import DBSCAN
from preprocessing import *
from utils import *

documents = []

def levenshteinMetric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return levenshtein(documents[i], documents[j])

def generateClustersDict(labels):
    clusters = {}
    n = 0

    for item in labels:
        if item in clusters:
            clusters[item].append(documents[n])
        else:
            clusters[item] = [documents[n]]
        n +=1

    for item in clusters:
        print("Cluster ", item)
        for i in clusters[item]:
            print(i)

def clusterize(metric):
    X = np.arange(len(documents)).reshape(-1, 1)
    db = DBSCAN(eps=20, min_samples=1, metric=metric).fit(X)

    clusters = generateClustersDict(db.labels_)

    return clusters

def main():
    # sourcefile = sys.argv[1]
    sourcefile = linesFile
    linesWithoutStopWords = performPreprocessing(sourcefile)
    linesWithoutStopWords = linesWithoutStopWords[0:100]

    global documents
    documents = linesWithoutStopWords

    levenshteinClusters = clusterize(levenshteinMetric)

if __name__ == "__main__":
    main()

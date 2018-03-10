import os
from utils import *

files = os.listdir(resultsIdentificationDir)

for datafile in files:
    output = os.path.splitext(datafile)[0] + '.svg'
    print(output)
    os.system('gnuplot -e \"datafile=\'' + resultsIdentificationDir + datafile
        + '\'; outputname=\'gnuplot/identification/' + output +'\'\" '
        + drawIdentificationScript)

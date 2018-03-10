import os
from utils import *

files = os.listdir(resultsStatsDir)
print(files)

for datafile in files:
    output = os.path.splitext(datafile)[0] + '.svg'
    print(output)
    os.system('gnuplot -e \"datafile=\'' + resultsStatsDir + datafile
        + '\'; outputname=\'gnuplot/stats/' + output +'\'\" '
        + drawStatsScript)

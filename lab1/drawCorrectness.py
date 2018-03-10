import os
from utils import *

output = os.path.splitext(resultsCorrenctnessFile)[0] + '.svg'
print(output)
datafile = resultsCorrenctnessDir + resultsCorrenctnessFile
outputfile = 'gnuplot/correctness/' + output

os.system('gnuplot -e \"datafile=\'' + datafile
    + '\'; outputname=\'' + outputfile +'\'\" '
    + drawCorrectnessScript)

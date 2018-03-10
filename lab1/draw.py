import os

files = os.listdir('results/')
print(files)

for datafile in files:
    output = os.path.splitext(datafile)[0] + '.svg'
    print(output)
    os.system('gnuplot -e \"datafile=\'results/' + datafile + '\'; outputname=\'gnuplot/' + output +'\'\" gnuplot/draw.plg')

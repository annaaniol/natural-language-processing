import os

files = os.listdir('results/')
print(files)

for f in files:
    datafile = 'results/' + os.path.splitext(f)[0]
    output = datafile + '.svg'
    print(output)
    os.system('gnuplot -e \"datafile=\'results/' + datafile + '\'; outputname=\'gnuplot/' + output +'\'\" gnuplot/draw.plg')

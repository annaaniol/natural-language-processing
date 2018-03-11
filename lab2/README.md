Some useful commands which have been used to adjust an output file for gnuplot:
```
awk '{print NR","$0}' results/potop.csv > results/newPotop.csv
mv results/newPotop.csv results/potop.csv

awk -F "," '$2 > 0 {print}' results/potop.csv > results/newPotop.csv
mv results/newPotop.csv results/potop.csv
```

To draw gnuplot charts:
```
gnuplot -e "datafile='results/potop.csv'; outputname='gnuplot/zipfsLaw100.svg'; maxRankNumber='100'" gnuplot/zipfsLaw.plg

gnuplot -e "datafile='results/potop.csv'; outputname='gnuplot/zipfsLaw1000.svg'; maxRankNumber='1000'" gnuplot/zipfsLaw.plg
```

To count hapax legomena and other occurrence stats:
```
python3 countOccurrenceStats.py
```

For "Potop" results are as follows:

> Hapax legomena:  3369

> All words with repetitions:  214117

> Unique words:  8529

> Unique words in 50% of text:  38

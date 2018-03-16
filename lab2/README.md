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

> Hapax legomena: 23653

> All words: 384570

> Unique words (reduced to primary form): 45468

> Unique words in 50% of the text: 355

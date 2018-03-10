import ngramStats

top = 30

for n in range (2,6):
    for lang in ['en', 'ge', 'fn', 'it', 'es', 'pl']:
        ngramStats.countStats(n, lang, top)

from collections import Counter

english = open('sources/english1.txt').read().lower()
english += open('sources/english2.txt').read().lower()
english += open('sources/english3.txt').read().lower()
english += open('sources/english4.txt', encoding='latin-1').read().lower()

n = 10

englishNgrams = []

for x in range(len(english)-n+1):
    englishNgrams.append(english[x:x+n])

print(Counter(englishNgrams).most_common(100))

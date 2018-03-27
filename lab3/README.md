### Abstract
The goal was to group all of the addresses as they are formatted differently from each other
but some of them point to the same real address.

Number of addresses in the analyzed file *sources/lines.txt* : 6751

### Preprocessing
#### Stop-list
Words, which are present in over 10% of lines:

[word] [number of lines containing the word]
- no 1111
- o 1107
- china 1451
- ltd 2416
- logistics 862
- road 1136
- co 1535
- sp 848
- russia 779
- a 779
- 7 726
- fax 1620
- ul 1107
- tel 2091
- poland 960
- z 742
- of 703

However, some of them are considered meaningful:

> poland, china, logistics, russia, 7

Therefore the basic stop words are:

> no, o, ltd, road, co, sp, a, fax, ul, tel, z, of

What could be done to improve the results:
1. better preprocessing
  - modify Levenshtein metric when both inputs shorter then clustering eps *done*
  - remove all phone numbers and emails (regex) *done*
  - always split numbers and letters with a space *done*
  - sort all string words alphabetically *done*
  - translate names to a base language (e.g. Warsaw -> Warszawa) *partially done*
  - change names to a base form (e.g. St-Petersburg -> Saint Petersburg) *partially done*
  - remove all spaces after all simplifications (unnecessary, give no information) *done*

### Run the script
```
python3 scripts/clusterization.py [file_to_analyze] [metric] [eps]
```
Supported metrics:
- Levenshtein *metric="lev"*
- Levenshtein-to-size (modified Levenshtein metric) *metric="levsize"*
- Longest_common_substring *metric="lcs"*
- Longest_common_substring-to-size (modified Longest_common_substring metric) *metric="lcssize"*

Example run command:
```
python3 scripts/clusterization.py sources/lines.txt lev 10
```


### Example results

levsize 0.3
> Estimated number of clusters: 4025
> Silhouette Coefficient: **0.382** - best of the achieved indexes

levsize 0.4
> Estimated number of clusters: 3572
> Silhouette Coefficient: 0.368

lev 10
> Estimated number of clusters: 4717
Silhouette Coefficient: 0.356

lev 15
> Estimated number of clusters: 4337
> Silhouette Coefficient: 0.358

#### Silhouette Coefficient meaning
From Sewell, Grandville, and P. J. Rousseau. "Finding groups in data: An introduction to cluster analysis." (1990)

> 0.71-1.0
A strong structure has been found

> 0.51-0.70
A reasonable structure has been found

> 0.26-0.50
The structure is weak and could be artificial. Try additional methods of data analysis.

> < 0.25
No substantial structure has been found

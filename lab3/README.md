Number of lines: 6751

Words, which are present in over 10% of lines:
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

Therefore the stop words are:

> no, o, ltd, road, co, sp, a, fax, ul, tel, z, of

To run:
```
python3 scripts/clusterization.py [file_to_analyze] [metric]
```
where metric should be one of:
"lev", "lcs", "lcssize"

Example run:
```
python3 scripts/clusterization.py sources/lines.txt lev
```

To get top X n-grams for a language:

`python3 ngramStats.py [n] [language shortcut] [X]`

e.g. to get top 30 english 5-grams:

`python3 ngramStats.py 5 en 30`

To generate n-grams base for further analysis:

`python3 generateTopNgrams.py`

To generate n-grams stats for all available languages:

`python3 countAllStats.py`

To generate analysis for language identification of available sentences:

`python3 identifyAllSentences.py`

To identify language of a sentence with n-ngrams:

`python3 identifyLanguage.py "[n]" "[sentence]"`

e.g.

`python3 identifyLanguage.py "3" "Siedzi wrona na ekierce."`

To draw charts:
```
python3 drawStats.py
python3 drawIdentification.py
python3 drawCorrectness.py
```

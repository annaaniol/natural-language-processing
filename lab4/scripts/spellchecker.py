import re
import collections
import sys
import threading
import wordranking as wr
import probability as prob
from utils import *

def train(features):
  model = collections.defaultdict(lambda: 1)
  for f in features:
    model[f] += 1
  return model

NWORDS_CORPUS = train(wr.get_all_words(CORPUS_FILE_NAME))
NWORDS_DICT = train(wr.get_all_words(DICTIONARY_FILE_NAME))

ALPHABET = 'aąbcćdeęfghijklłmnoópqrsśtuvwxyzźż'

def edits1(word):
  splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
  deletes = [a + b[1:] for a, b in splits if b]
  transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
  replaces = [a + c + b[1:] for a, b in splits for c in ALPHABET if b]
  inserts = [a + c + b for a, b in splits for c in ALPHABET]
  return set(deletes + transposes + replaces + inserts)

def edits2(word):
  splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
  deletes = [a + b[2:] for a, b in splits if b]
  replaces = [a[1:] + c + b[1:] + d for a, b in splits for c in ALPHABET for d in ALPHABET if a and b]
  inserts = [a + c  + d + b for a, b in splits for c in ALPHABET for d in ALPHABET]
  return set(deletes + replaces + inserts)

def known_dict(words): return set(w for w in words if w in NWORDS_DICT)
def known_corpus(words): return set(w for w in words if w in NWORDS_CORPUS)

def back_upper(correction):
    correction = list(correction)
    correction[0] = correction[0].upper()
    correction = ''.join(correction)
    return correction

def check(word):
    starts_with_upper = word[0].isupper()
    word = word.lower()

    if known_corpus([word]) or known_dict([word]):
        if starts_with_upper:
            correction = back_upper(word)
            print(correction, 'is OK')
        else:
            correction = word
            print(correction, 'is OK')
    else:
        candidates = known_corpus(edits1(word)) or known_dict(edits1(word)) or known_corpus(edits2(word)) or known_dict(edits2(word)) or [word]
        print(candidates)
        max_prob = 0
        correction = ''

        for c in candidates:
            new_prob = prob.probability_cw(word,c)
            print(c, new_prob)
            if new_prob > max_prob:
                correction = c
                max_prob = new_prob

        correction = back_upper(correction) if starts_with_upper else correction
        print(correction)

    return correction

def is_valid(word):
    pattern = re.compile('[a-zA-Z|(ąćęłńóśźżĄĆĘŁŃÓŚŹŻ)]+')
    if pattern.match(word) and len(pattern.match(word)[0]) == len(word):
        return True
    return False

def main():

    while True:
        word = input('--> ')
        if is_valid(word):
            check(word)
        else:
            print("Please specify a valid word")


if __name__ == "__main__":
    main()

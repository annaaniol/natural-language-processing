import sys
import wordranking as wr
from utils import *

# works for QWERTY keyboard layout
def get_keys_around(key):
    key = key.lower()
    keys = []
    polish_latin_map = {
        'ą':'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'x',
        'ż': 'z'
    }
    for polish, latin in polish_latin_map.items():
        if key == polish:
            key = latin

    lines = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
    line_index, index = [(i, l.find(key)) for i, l in enumerate(lines) if key in l][0]
    lines = lines[0: 3]
    steps = [-1, 0, 1]
    for line_step in steps:
        keys.extend([
                lines[line_index+line_step][index+letter_step] for letter_step in [step for step in steps if step != line_step]
                if line_index+line_step >= 0 and len(lines[line_index+line_step]) > index + letter_step and index + letter_step >= 0
            ])
    return keys

def custom_levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    elif t[-1] in get_keys_around(s[-1]):
        cost = 1
    else:
        cost = 2

    res = min([custom_levenshtein(s[:-1], t)+1,
               custom_levenshtein(s, t[:-1])+1,
               custom_levenshtein(s[:-1], t[:-1]) + cost])
    return res

def probability_wc(word, correction):
    distance = custom_levenshtein(word, correction)
    if distance == 0:
        return 1
    else:
        return 1/(distance*26)

def probality_c(word, alpha):
    nc = wr.get_word_occurences_count(word, RANK_FILE_NAME, CORPUS_FILE_NAME)
    n = wr.get_all_words_in_corpus_count(CORPUS_FILE_NAME)
    m = wr.get_dictionary_size(DICTIONARY_FILE_NAME)
    return (nc+alpha)/(n+alpha*m)

def main():
    word = str(sys.argv[1])
    correction = str(sys.argv[2])

    probability = probability_wc(word, correction)
    print('Probability of typing {0:s} when {1:s} was intended: {2:.2%}'.format(word, correction, probability))

    pc =  probality_c(correction, 10)
    print('Proability of using {0:s}: {1:.5%}'.format(correction, pc))

if __name__ == "__main__":
    main()

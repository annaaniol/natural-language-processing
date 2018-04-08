import sys
import wordranking as wr
from utils import *

ALPHA = 100
ALPHABET_SIZE = 35
N = wr.get_all_words_in_corpus_count(CORPUS_FILE_NAME)
M = wr.get_dictionary_size(DICTIONARY_FILE_NAME)

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

def memoize(func):
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer

# works for QWERTY keyboard layout
def get_keys_around(key):
    key = key.lower()
    keys = []
    polish_latin_map = {
        'ą': 'a',
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
            keys.append(latin)
            key = latin
        elif key == latin:
            keys.append(polish)

    lines = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
    line_index, index = [(i, l.find(key)) for i, l in enumerate(lines) if key in l][0]
    lines = lines[0: 3]
    steps = [-1, 0, 1]
    for line_step in steps:
        keys.extend([
                lines[line_index+line_step][index+letter_step] for letter_step in [step for step in steps if step != line_step]
                if line_index+line_step in range (0,3) and len(lines[line_index+line_step]) > index + letter_step and index + letter_step >= 0
            ])
    return keys

@call_counter
@memoize
def custom_levenshtein(s, t):
    if s == "":
        return 2 * len(t)
    elif t == "":
        return 2 * len(s)
    elif s[-1] == t[-1]:
        cost = 0
    elif t[-1] in get_keys_around(s[-1]):
        cost = 1
    else:
        cost = 2

    res = min([custom_levenshtein(s[:-1], t) + 2,
               custom_levenshtein(s, t[:-1]) + 2,
               custom_levenshtein(s[:-1], t[:-1]) + cost])

    return res

def probability_wc(word, correction):
    distance = custom_levenshtein(word, correction)/2
    if distance == 0:
        return 1
    else:
        return 1/(distance*ALPHABET_SIZE)

def probability_c(word, alpha):
    nc = wr.get_word_occurences_count(word, RANK_FILE_NAME, CORPUS_FILE_NAME)
    n = N
    m = M
    return (nc+alpha)/(n+alpha*m)

def probability_cw(word, correction):
    pwc = probability_wc(word, correction)
    pc = probability_c(correction, ALPHA)

    return pwc * pc * 1000000

def main():
    word = str(sys.argv[1])
    correction = str(sys.argv[2])

    pwc = probability_wc(word, correction)
    print('Probability of typing {0:s} when {1:s} was intended: {2:.2%}'.format(word, correction, pwc))

    pc =  probability_c(correction, ALPHA)
    print('Proability of using {0:s}: {1:.5%}'.format(correction, pc))

    pcw = probability_cw(word, correction)
    print('Proability of correction {0:s} -> {1:s}: {2:.10%}'.format(word, correction, pcw))

    print(custom_levenshtein(word,correction))

if __name__ == "__main__":
    main()

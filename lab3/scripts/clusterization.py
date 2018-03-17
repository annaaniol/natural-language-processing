import string
from preprocessing import *

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

@call_counter
@memoize
def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t)+1,
               levenshtein(s, t[:-1])+1,
               levenshtein(s[:-1], t[:-1]) + cost])
    return res

def main():
    # sourcefile = sys.argv[1]
    sourcefile = linesFile
    linesWithoutStopWords = performPreprocessing(sourcefile)
    print(levenshtein("ala ma kota, ale rudego", "ala ma psa który jest czarny"))
    print(levenshtein("abababa", "abababa 22"))


if __name__ == "__main__":
    main()

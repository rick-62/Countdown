import json
from collections import Counter
from operator import itemgetter

def load_words(mx=9):
    with open("large.txt") as f:
        words = set(w for w in f.read().split() if len(w) <= mx)
    return words

class Solve:
    all_words = load_words()

    def __init__(self, jumble):
        self.jumble = jumble.lower()
        self.solution = self._solution()

    def top(self, top):
        return self.solution[:top]

    def _solution(self):
        dct = {}
        for word in self.all_words:
            if self._is_found(word):
                dct[word] = len(word)
        return sorted(dct.items(), key=itemgetter(1), reverse=True)

    def _is_found(self, a):
        count_a = Counter(a) 
        count_b = Counter(self.jumble) 
        for key in count_a: 
            if key not in count_b: 
                return False
            if count_b[key] < count_a[key]: 
                return False
        return True

    def __repr__(self):
        r = \
        """
        Initial jumble: {}
        Best solution: {} ({} letters)
        Total solutions: {}
        """.format(self.jumble, 
                   self.solution[0][0], 
                   self.solution[0][1], 
                   len(self.solution))
        return r

    def __str__(self):
        return self.__repr__()


class Words:
    all_words = load_words()

    def __init__(self):
        self.chunks = Chunks(self.all_words)


class Chunks:

    def __init__(self, word_list):
        self.word_list = word_list
        self.chunks = self._make_chunks()

    def most_common(self, length, top):
        subset = {k:v for k,v in self.chunks.items() if len(k) == length}
        return sorted(subset.items(), key=itemgetter(1), reverse=True)[:top]

    def _make_chunks(self):
        cnks = Counter()
        for w in self.word_list:
            split = set([w[i:j+1] for i in range(len(w)) for j in range(i,len(w))])
            curr_cnt = Counter(split)
            cnks.update(curr_cnt)
        self.chunks = cnks
        return cnks

    


    


    


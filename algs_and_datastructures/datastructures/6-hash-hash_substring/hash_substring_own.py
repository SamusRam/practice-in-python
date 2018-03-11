# python3
import sys
import random
from functools import reduce

class RabinKarp():

    def __init__(self):
        self.pattern = input().rstrip()
        self.text = input().rstrip()
        self.p = 1000000007
        self.x = 263
        self.pattern_len = len(self.pattern)

        self.pHash = self.compute_hash(self.pattern, 0, self.pattern_len)
        self.precomputed_hashes = self.precompute()

    def compute_hash(self, text, position, length):
        result = reduce(lambda hash, i: (ord(text[position + i]) + hash * self.x) % self.p, range(length-1, -1, -1), 0)
        return result

    def precompute(self):
        last_value = self.compute_hash(self.text, len(self.text) - self.pattern_len, self.pattern_len)
        results = [-1] * (len(self.text) - self.pattern_len + 1)
        results[-1] = last_value

        y = reduce(lambda x, _: (x * self.x) % self.p, range(self.pattern_len), 1)

        for position in range(len(self.text) - self.pattern_len - 1, -1, -1):
            results[position] = (self.x * results[position + 1] + ord(self.text[position]) - y * ord(self.text[position + self.pattern_len])) % self.p
        return results

    def find_occurrences(self):
        indices_of_occurrences = (str(i) for i in range(len(self.text) - self.pattern_len + 1)
                                  if self.precomputed_hashes[i] == self.pHash and
                                  self.text[i: i + self.pattern_len] == self.pattern)
        print(' '.join(indices_of_occurrences))

if __name__ == '__main__':
    worker = RabinKarp()
    worker.find_occurrences()




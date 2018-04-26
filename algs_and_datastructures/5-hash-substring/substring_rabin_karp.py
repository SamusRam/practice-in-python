# python3
from functools import reduce
import sys
import unittest
import os
import io


class RabinKarp:

    def __init__(self):
        self.pattern = sys.stdin.readline().rstrip()
        self.text = sys.stdin.readline().rstrip()
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


class Tester(unittest.TestCase):

    def test_all_scenarios(self):
        path_to_test_cases = os.path.join(os.getcwd(), 'tests')
        input_file_names = [f for f in os.listdir(path_to_test_cases)
                            if os.path.isfile(os.path.join(path_to_test_cases, f)) and f[-2:] != '.a']
        current_stdin = sys.stdin
        current_stdout = sys.stdout

        try:
            for file in input_file_names:
                file_path = os.path.join(path_to_test_cases, file)
                sys.stdout = io.StringIO()
                with open(file_path, 'r') as file_object:
                    sys.stdin = file_object
                    worker_instance = RabinKarp()
                    worker_instance.find_occurrences()
                instance_output = sys.stdout.getvalue()
                answer_file_path = os.path.join(path_to_test_cases, file + '.a')
                with open(answer_file_path, 'r') as answer_file_object:
                    correct_output = answer_file_object.read()
                self.assertEqual(instance_output if instance_output != '\n' else '',
                                 correct_output, 'test on file ' + file)
        finally:
            sys.stdin = current_stdin
            sys.stdout = current_stdout

if __name__ == '__main__':
    unittest.main()
    # worker = RabinKarp()
    # worker.find_occurrences()




# python3
import sys
import unittest
import os
import io


class MergeTables:

    def __init__(self):
        self.number_of_tables, self.number_of_queries = [int(x) for x in sys.stdin.readline().split()]
        self.sizes = [int(x) for x in sys.stdin.readline().split()]
        self.ranks = [1 for _ in range(self.number_of_tables)]
        self.parent = list(range(self.number_of_tables))
        self.max_size = max(self.sizes)

    def do_job(self):
        for _ in range(self.number_of_queries):
            self.process_query()

    def process_query(self):
        source, destination = [int(x) for x in sys.stdin.readline().split()]
        self.union(source - 1, destination - 1)
        print(self.max_size)

    def union(self, source, target):
        group_1 = self.find(source)
        group_2 = self.find(target)
        if group_1 != group_2:
            larger = max(group_1, group_2, key=lambda x: (self.ranks[x], x))
            smaller = min(group_1, group_2, key=lambda x: (self.ranks[x], x))
            self.parent[smaller] = larger
            self.ranks[larger] = max(self.ranks[larger], self.ranks[smaller] + 1)
            self.sizes[larger] += self.sizes[smaller]
            self.max_size = max(self.sizes[larger], self.max_size)

    def find(self, i):
        group_rep = i
        while group_rep != self.parent[group_rep]:
            group_rep = self.parent[group_rep]

        # path compression
        if i != group_rep:
            next_item = self.parent[i]
            current = i
            while next_item != group_rep:
                self.parent[current] = group_rep
                self.ranks[group_rep] = max(self.ranks[group_rep], self.ranks[current] + 1)
                current = next_item
                next_item = self.parent[current]
        return group_rep

    def find_rec(self, i):
        if i != self.parent[i]:
            group_rep = self.find_rec(self.parent[i])
            self.parent[i] = group_rep
            self.ranks[group_rep] = max(self.ranks[group_rep], self.ranks[i] + 1)

        return self.parent[i]


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
                    worker_instance = MergeTables()
                    worker_instance.do_job()
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
    # worker = MergeTables()
    # worker.do_job()

# python3
import sys
import unittest
import io
import os


class BellmanFordNegCycleDetector:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            next_start_vertex, next_end_vertex, weight = map(int, sys.stdin.readline().split())
            self.adj_list[next_start_vertex - 1].append((next_end_vertex - 1, weight))
        self.distances = [sys.maxsize] * self.n
        self.next_starting_vertex = 0

    def contains_neg_cycle(self):
        while self.next_starting_vertex is not None:
            self.distances[self.next_starting_vertex] = 0

            iteration = 0
            change_occurred = True
            while iteration < self.n - 1 and change_occurred:
                change_occurred = False
                iteration += 1
                for vertex in range(self.n):
                    for neighbour, weight in self.adj_list[vertex]:
                        if self.distances[neighbour] > self.distances[vertex] + weight:
                            self.distances[neighbour] = self.distances[vertex] + weight
                            change_occurred = True

            for vertex in range(self.n):
                for neighbour, weight in self.adj_list[vertex]:
                    if self.distances[neighbour] > self.distances[vertex] + weight:
                        self.distances[neighbour] = self.distances[vertex] + weight
                        return True

            self.next_starting_vertex = next(filter(lambda v: self.distances[v] == sys.maxsize, range(self.n)), None)

        return False

    def do_job(self):
        result = 1 if self.contains_neg_cycle() else 0
        print(result)


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
                    worker_instance = BellmanFordNegCycleDetector()
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
    worker = BellmanFordNegCycleDetector()
    worker.do_job()

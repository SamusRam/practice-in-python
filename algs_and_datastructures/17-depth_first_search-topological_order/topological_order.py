# python 3
import sys
import unittest
import io
import os


class TopologicalOrder:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            [vertex_source, vertex_dist] = map(lambda i: int(i) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_source].append(vertex_dist)
        self.not_closed = set(range(self.n))
        self.reversed_topological_order = []

    def dfs(self, node_idx):
        for neighbour in self.adj_list[node_idx]:
            if neighbour in self.not_closed:
                self.dfs(neighbour)
        self.reversed_topological_order.append(node_idx)
        self.not_closed.remove(node_idx)

    def get_topological_order(self):
        while len(self.not_closed):
            self.dfs(next(iter(self.not_closed)))
        return reversed(self.reversed_topological_order)

    def do_job(self):
        print(" ".join(map(lambda i: str(i + 1), self.get_topological_order())))


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
                    worker_instance = TopologicalOrder()
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
    worker = TopologicalOrder()
    worker.do_job()

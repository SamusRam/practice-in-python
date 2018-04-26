# python 3
import sys
import unittest
import io
import os


class CounterCC:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        self.parent = [-1] * self.n
        for _ in range(self.m):
            [vertex_one, vertex_two] = map(lambda x: int(x) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_one].append(vertex_two)
            self.adj_list[vertex_two].append(vertex_one)
        self.opened = set(range(self.n))

    def dfs(self, node_idx):
        for neighbour in self.adj_list[node_idx]:
            if neighbour in self.opened:
                self.opened.remove(neighbour)
                self.dfs(neighbour)

    def count_connected_components(self):
        cc_count = 0
        while len(self.opened):
            self.dfs(self.opened.pop())
            cc_count += 1
        return cc_count


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
                    worker_instance = CounterCC()
                    print(worker_instance.count_connected_components())
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
    worker = CounterCC()
    print(worker.count_connected_components())
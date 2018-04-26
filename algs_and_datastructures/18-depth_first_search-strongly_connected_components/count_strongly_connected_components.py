# python 3
import sys
import threading
import unittest
import io
import os
sys.setrecursionlimit(2**27)
threading.stack_size(2**27)


class SccCounter:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        self.adj_list_reversed = [[] for _ in range(self.n)]
        for _ in range(self.m):
            [vertex_source, vertex_dist] = map(lambda i: int(i) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_source].append(vertex_dist)
            self.adj_list_reversed[vertex_dist].append(vertex_source)
        self.processing_order = []

    def determine_processing_order(self):
        not_processed = set(range(self.n))
        opened = set()

        def dfs(node_idx):
            opened.add(node_idx)
            for neighbour in self.adj_list_reversed[node_idx]:
                if neighbour not in opened:
                    dfs(neighbour)
            not_processed.remove(node_idx)
            self.processing_order.append(node_idx)

        while len(not_processed):
            dfs(next(iter(not_processed)))
        self.processing_order = reversed(self.processing_order)

    def count_scc_print(self):
        self.determine_processing_order()
        discovered_nodes = set()

        def dfs(node_idx):
            discovered_nodes.add(node_idx)
            for neighbour in self.adj_list[node_idx]:
                if neighbour not in discovered_nodes:
                    dfs(neighbour)

        counter = 0
        for next_node in self.processing_order:
            if next_node not in discovered_nodes:
                counter += 1
                dfs(next_node)
        print(counter)

    def do_job(self):
        threading.Thread(target=self.count_scc_print()).start()


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
                    worker_instance = SccCounter()
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
    # unittest.main()
    worker = SccCounter()
    worker.do_job()

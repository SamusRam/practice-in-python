# python 3
import sys
import unittest
import io
import os


class AcyclicityChecker:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            [vertex_one, vertex_two] = map(lambda i: int(i) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_one].append(vertex_two)
        self.opened_set = set()
        self.not_processed = set(range(self.n))

    def cycle_in_cc_by_dfs(self, node_idx):
        if node_idx in self.opened_set:
            return True
        self.opened_set.add(node_idx)
        for neighbour in self.adj_list[node_idx]:
            if neighbour in self.not_processed and self.cycle_in_cc_by_dfs(neighbour):
                return True
        self.not_processed.remove(node_idx)

    def topological_sort_acyclicity_check(self):
        while len(self.not_processed):
            if self.cycle_in_cc_by_dfs(next(iter(self.not_processed))):
                return False
        return True

    def do_job(self):
        result = 0 if self.topological_sort_acyclicity_check() else 1
        print(result)

    '''
    def naive_acyclicity_check(self):
        for node_idx in range(self.n):
            if self.has_cycle_with_node(node_idx):
                return False
        return True  

    def has_cycle_with_node(self, node_idx):
        discovered = {node_idx}
        closed = set()
        while len(discovered):
            next_node = discovered.pop()
            closed.add(next_node)
            for neighbour in self.adj_list[next_node]:
                if neighbour == node_idx:
                    return True
                if neighbour not in closed:
                    discovered.add(neighbour)
    '''


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
                    worker_instance = AcyclicityChecker()
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
    worker = AcyclicityChecker()
    worker.do_job()

# python 3
import sys
from collections import deque
import unittest
import os
import io


class BfsBasedChecker:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            [vertex_one, vertex_two] = map(lambda i: int(i) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_one].append(vertex_two)
            self.adj_list[vertex_two].append(vertex_one)
        self.not_visited_set = set(range(self.n))
        self.node_levels = [-1] * self.n

    def bipartite_check(self):
        is_bipartite = True
        starting_level_number = 0
        while is_bipartite and len(self.not_visited_set):
            first_node = next(iter(self.not_visited_set))
            self.node_levels[first_node] = starting_level_number
            queue = deque([first_node])
            while len(queue):
                current_node = queue.popleft()
                current_node_level = self.node_levels[current_node]
                self.not_visited_set.remove(current_node)
                for neighbour in self.adj_list[current_node]:
                    if neighbour in self.not_visited_set:
                        if self.node_levels[neighbour] == -1:
                            queue.append(neighbour)
                            self.node_levels[neighbour] = current_node_level + 1
                        elif self.node_levels[neighbour] == current_node_level:
                            is_bipartite = False
                            break
        return is_bipartite

    def do_job(self):
        if self.bipartite_check():
            print(1)
        else:
            print(0)


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
                    worker_instance = BfsBasedChecker()
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
    worker = BfsBasedChecker()
    worker.do_job()





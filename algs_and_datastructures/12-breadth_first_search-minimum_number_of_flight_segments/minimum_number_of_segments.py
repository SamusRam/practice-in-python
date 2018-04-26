# python 3
import sys
from collections import deque
import unittest
import os
import io


class Bfs:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            [vertex_one, vertex_two] = map(lambda i: int(i) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_one].append(vertex_two)
            self.adj_list[vertex_two].append(vertex_one)
        [self.start, self.target] = map(lambda i: int(i) - 1, sys.stdin.readline().split())
        self.visited = set()

    def find_closest_path(self):
        queue = deque([(self.start, 0)]) # each element is in format (node, distance from the start node)
        target_distance = None
        while len(queue) and not target_distance:
            [next_node, distance_from_source] = queue.popleft()
            for neighbour in self.adj_list[next_node]:
                next_distance_from_source = distance_from_source + 1
                if neighbour not in self.visited:
                    self.visited.add(neighbour)
                    if neighbour != self.target:
                        queue.append((neighbour, next_distance_from_source))
                    else:
                        target_distance = next_distance_from_source
                        break
        if not target_distance:
            return -1
        else:
            return target_distance

    def do_job(self):
        print(self.find_closest_path())


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
                    worker_instance = Bfs()
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
    # worker = Bfs()
    # worker.do_job()


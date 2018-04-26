# python 3
import sys
from collections import deque
import unittest
import io
import os


class MazeEvaluator:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        # self.parent = [-1] * self.n
        for _ in range(self.m):
            [vertex_one, vertex_two] = map(lambda x: int(x) - 1, sys.stdin.readline().split())
            self.adj_list[vertex_one].append(vertex_two)
            self.adj_list[vertex_two].append(vertex_one)
        [self.start, self.finish] = map(lambda x: int(x) - 1, sys.stdin.readline().split())

    # breadth_first_search-minimum_number_of_flight_segments-based check
    def check_goal_reachability(self):
        queue = deque([self.start])
        closed_nodes = {self.start}
        found_path = self.start == self.finish
        while len(queue) > 0 and not found_path:
            next_node = queue.popleft()
            for neighbour in self.adj_list[next_node]:
                if neighbour not in closed_nodes:
                    closed_nodes.add(neighbour)
                    queue.append(neighbour)
                    # self.parent[neighbour] = next_node
                    found_path = found_path or neighbour == self.finish

        # if found_path:
        #     prev_node = self.finish
        #     while prev_node != self.start:
        #         print(str(prev_node + 1))
        #         prev_node = self.parent[prev_node]
        return found_path

    def do_job(self):
        result = 1 if self.check_goal_reachability() else 0
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
                    worker_instance = MazeEvaluator()
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
    worker = MazeEvaluator()
    worker.do_job()



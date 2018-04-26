# python3
import sys
from collections import deque
import unittest
import io
import os


class BellmanFordNegShortPaths:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            next_start_vertex, next_end_vertex, weight = map(int, sys.stdin.readline().split())
            self.adj_list[next_start_vertex - 1].append((next_end_vertex - 1, weight))
        self.distances = [sys.maxsize] * self.n
        self.starting_vertex = int(sys.stdin.readline()) - 1
        self.distances[self.starting_vertex] = 0

    def bfs_get_neg_cycle_reachable_vertices(self, opened_queue):
        closed_set = set()
        while len(opened_queue):
            next_vertex = opened_queue.popleft()
            closed_set.add(next_vertex)
            self.distances[next_vertex] = -sys.maxsize
            for neighbour, _ in self.adj_list[next_vertex]:
                if neighbour not in closed_set:
                    opened_queue.append(neighbour)

    def compute_distances_reachability_via_neg_cycles(self):
        iteration = 0
        change_occurred = True
        while iteration < self.n - 1 and change_occurred:
            change_occurred = False
            iteration += 1
            for vertex in range(self.n):
                if self.distances[vertex] != sys.maxsize:
                    for neighbour, weight in self.adj_list[vertex]:
                        if self.distances[neighbour] > self.distances[vertex] + weight:
                            self.distances[neighbour] = self.distances[vertex] + weight
                            change_occurred = True

        # there can be neg cycles only if change_occurred == True
        # if change_occurred:
        opened_neg_cycle_queue = deque([])
        for vertex in range(self.n):
            if self.distances[vertex] != sys.maxsize:
                for neighbour, weight in self.adj_list[vertex]:
                    # if contains neg cycle with the node 'neighbour' on it
                    if self.distances[neighbour] > self.distances[vertex] + weight:
                        self.distances[neighbour] = self.distances[vertex] + weight
                        opened_neg_cycle_queue.append(neighbour)
        self.bfs_get_neg_cycle_reachable_vertices(opened_neg_cycle_queue)

    def do_job(self):
        self.compute_distances_reachability_via_neg_cycles()
        for vertex in range(self.n):
            dist = self.distances[vertex]
            result = '*' if dist == sys.maxsize else '-' if dist == -sys.maxsize else dist
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
                    worker_instance = BellmanFordNegShortPaths()
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
    worker = BellmanFordNegShortPaths()
    worker.do_job()

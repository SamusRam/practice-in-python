# python3
import sys
import unittest
import io
import os


class DijkstraMinWeight:

    def __init__(self):
        [self.n, self.m] = map(int, sys.stdin.readline().split())
        self.adj_list = [[] for _ in range(self.n)]
        for _ in range(self.m):
            next_start_vertex, next_end_vertex, weight = map(int, sys.stdin.readline().split())
            self.adj_list[next_start_vertex - 1].append((next_end_vertex - 1, weight))
        self.start_vertex, self.target_vertex = map(lambda x: int(x) - 1, sys.stdin.readline().split())

    def dijkstra_shortest_path_len(self):
        priority_queue = Heap()
        current_min_distances = [sys.maxsize] * self.n
        priority_queue.insert(self.start_vertex, 0)
        current_min_distances[self.start_vertex] = 0
        while priority_queue.non_empty():
            current_vertex, current_distance = priority_queue.pop_min()
            if current_vertex == self.target_vertex:
                break
            for neighbour, weight in self.adj_list[current_vertex]:
                if current_distance + weight < current_min_distances[neighbour]:
                    if current_min_distances[neighbour] == sys.maxsize:
                        priority_queue.insert(neighbour, current_distance + weight)
                    else:
                        priority_queue.decrease_value(neighbour, current_distance + weight)
                    current_min_distances[neighbour] = current_distance + weight

        if current_min_distances[self.target_vertex] == sys.maxsize:
            return -1
        return current_min_distances[self.target_vertex]

    def do_job(self):
        print(self.dijkstra_shortest_path_len())


class Heap:
    def __init__(self):
        self.heap_values = []
        self.heap_identifiers = []
        self.heap_identifier_2_idx = dict()

    def swap_at_positions(self, idx1, idx2):
        self.heap_values[idx1], self.heap_values[idx2] = \
            self.heap_values[idx2], self.heap_values[idx1]
        self.heap_identifiers[idx1], self.heap_identifiers[idx2] = \
            self.heap_identifiers[idx2], self.heap_identifiers[idx1]
        self.heap_identifier_2_idx[self.heap_identifiers[idx1]], self.heap_identifier_2_idx[self.heap_identifiers[idx2]] = \
            self.heap_identifier_2_idx[self.heap_identifiers[idx2]], self.heap_identifier_2_idx[self.heap_identifiers[idx1]]

    def heapify(self, idx=0):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2

        min_idx = idx
        if left_child_idx < len(self.heap_values) and \
                        self.heap_values[left_child_idx] < self.heap_values[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self.heap_values) and \
                        self.heap_values[right_child_idx] < self.heap_values[min_idx]:
            min_idx = right_child_idx

        if min_idx != idx:
            self.swap_at_positions(idx, min_idx)
            self.heapify(min_idx)

    def move_up(self, idx):
        parent_idx = (idx - 1) // 2
        while parent_idx >= 0 and self.heap_values[idx] < self.heap_values[parent_idx]:
            self.swap_at_positions(parent_idx, idx)
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def insert(self, identifier, value):
        self.heap_identifiers.append(identifier)
        self.heap_values.append(value)
        self.heap_identifier_2_idx[identifier] = len(self.heap_identifier_2_idx)
        inserted_element_idx = len(self.heap_values) - 1
        self.move_up(inserted_element_idx)

    def decrease_value(self, identifier, new_value):
        current_idx = self.heap_identifier_2_idx[identifier]
        self.heap_values[current_idx] = new_value
        self.move_up(current_idx)

    def pop_min(self):
        candidate_id, candidate_value = self.heap_identifiers[0], self.heap_values[0]
        if len(self.heap_values) > 1:
            self.swap_at_positions(0, len(self.heap_values) - 1)
            identifier_to_remove, _ = self.heap_identifiers.pop(), self.heap_values.pop()
            self.heap_identifier_2_idx.pop(identifier_to_remove)
            self.heapify()
        else:
            self.heap_identifiers.pop(), self.heap_values.pop(), self.heap_identifier_2_idx.popitem()
        return candidate_id, candidate_value

    def non_empty(self):
        return len(self.heap_values) > 0


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
                    worker_instance = DijkstraMinWeight()
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
    worker = DijkstraMinWeight()
    worker.do_job()

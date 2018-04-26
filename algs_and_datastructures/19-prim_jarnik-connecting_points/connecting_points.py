# python3
import sys
import math
import unittest
import io
import os


class MstConnector:

    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(self.n)]
        self.adj_list = [[] for _ in range(self.n)]
        for vertex_one in range(self.n):
            for vertex_two in range(vertex_one + 1, self.n):
                dist = self.euclidean_dist(vertex_one, vertex_two)
                self.adj_list[vertex_one].append((vertex_two, dist))
                self.adj_list[vertex_two].append((vertex_one, dist))

    def euclidean_dist(self, idx_1, idx_2):
        return math.sqrt((self.points[idx_1][0] - self.points[idx_2][0])**2 +
                         (self.points[idx_1][1] - self.points[idx_2][1])**2)

    def prim_mst_cost(self):
        priority_queue = Heap()
        cost_of_being_connected = [float('inf')] * self.n
        starting_vertex = 0
        cost_of_being_connected[starting_vertex] = 0
        priority_queue.insert(starting_vertex, 0)
        total_cost = 0
        closed_vertices = set()
        opened_vertices = {starting_vertex}
        while priority_queue.non_empty():
            vertex, cost_of_adding = priority_queue.pop_min()
            total_cost += cost_of_adding
            closed_vertices.add(vertex)
            opened_vertices.remove(vertex)
            for neighbour, edge_weight in self.adj_list[vertex]:
                if neighbour not in closed_vertices and cost_of_being_connected[neighbour] > edge_weight:
                    cost_of_being_connected[neighbour] = edge_weight
                    if neighbour in opened_vertices:
                        priority_queue.decrease_value(neighbour, edge_weight)
                    else:
                        priority_queue.insert(neighbour, edge_weight)
                        opened_vertices.add(neighbour)
        return total_cost

    def do_job(self):
        print('{:.7f}'.format(self.prim_mst_cost()))


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
                    worker_instance = MstConnector()
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
    worker = MstConnector()
    worker.do_job()

# python3
import sys
import math
import unittest
import io
import os


class SeparatingClustersDistanceChecker:

    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(self.n)]
        self.k = int(sys.stdin.readline())

        self.edge_priority_queue = Heap()
        for vertex_one in range(self.n):
            for vertex_two in range(vertex_one + 1, self.n):
                edge_len = self.euclidean_dist(vertex_one, vertex_two)
                self.edge_priority_queue.insert((vertex_one, vertex_two), edge_len)

        self.union_find_checker = UnionFind(self.n)

    def euclidean_dist(self, idx_1, idx_2):
        return math.sqrt((self.points[idx_1][0] - self.points[idx_2][0])**2 +
                         (self.points[idx_1][1] - self.points[idx_2][1])**2)

    def find_max_separating(self):
        # a la Kruskal
        number_of_clusters = self.n
        while number_of_clusters >= self.k:
            (vertex_1, vertex_2), weight = self.edge_priority_queue.pop_min()
            while self.union_find_checker.belong_to_one_group(vertex_1, vertex_2):
                (vertex_1, vertex_2), weight = self.edge_priority_queue.pop_min()
            self.union_find_checker.union(vertex_1, vertex_2)
            number_of_clusters -= 1
        return weight

    def do_job(self):
        print('{:.9f}'.format(self.find_max_separating()))


class UnionFind:

    def __init__(self, n):
        self.size = n
        self.parent = list(range(self.size))
        self.rank = [0] * self.size

    def find_representer(self, idx):
        current_idx = idx
        while current_idx != self.parent[current_idx]:
            current_idx = self.parent[current_idx]
        group_representer = current_idx

        if group_representer != idx:
            while idx != group_representer:
                self.parent[idx] = group_representer
                idx = self.parent[idx]

        return group_representer

    def union(self, idx_1, idx_2):
        representer_1 = self.find_representer(idx_1)
        representer_2 = self.find_representer(idx_2)

        if representer_1 != representer_2:
            smaller_group_representer = min(representer_1, representer_2,
                                            key=lambda x: (self.rank[x], x))
            larger_group_representer = max(representer_1, representer_2,
                                           key=lambda x: (self.rank[x], x))
            self.parent[smaller_group_representer] = larger_group_representer
            # performing path compression during each find_representer run, it is ensured that heights are equal to 1.
            # Rank is size
            self.rank[larger_group_representer] += self.rank[smaller_group_representer]

    def belong_to_one_group(self, idx_1, idx_2):
        return self.find_representer(idx_1) == self.find_representer(idx_2)


class Heap:
    def __init__(self):
        self.heap_values = []
        self.heap_identifiers = []

    def swap_at_positions(self, idx1, idx2):
        self.heap_values[idx1], self.heap_values[idx2] = \
            self.heap_values[idx2], self.heap_values[idx1]
        self.heap_identifiers[idx1], self.heap_identifiers[idx2] = \
            self.heap_identifiers[idx2], self.heap_identifiers[idx1]

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
        inserted_element_idx = len(self.heap_values) - 1
        self.move_up(inserted_element_idx)

    def pop_min(self):
        candidate_id, candidate_value = self.heap_identifiers[0], self.heap_values[0]
        if len(self.heap_values) > 1:
            self.swap_at_positions(0, len(self.heap_values) - 1)
            identifier_to_remove, _ = self.heap_identifiers.pop(), self.heap_values.pop()
            self.heapify()
        else:
            self.heap_identifiers.pop(), self.heap_values.pop()
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
                    worker_instance = SeparatingClustersDistanceChecker()
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
    worker = SeparatingClustersDistanceChecker()
    worker.do_job()

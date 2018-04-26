# python3
import sys
from math import floor
import unittest
import os
import io


class BuildHeap:

    def __init__(self):
        self.data = []
        self.swaps = []

    def read_data(self):
        n = int(sys.stdin.readline())
        self.data = [int(x) for x in sys.stdin.readline().split()]
        assert n == len(self.data)

    def heapify(self, i):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        min_idx = i
        if left_child_idx < len(self.data) and self.data[left_child_idx] < self.data[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self.data) and self.data[right_child_idx] < self.data[min_idx]:
            min_idx = right_child_idx
        if min_idx != i:
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.swaps.append((i, min_idx))
            self.heapify(min_idx)

    def build_heap(self):
        for i in range(int(floor(len(self.data)/2)) - 1, -1, -1):
            self.heapify(i)

    def print_results(self):
        print(len(self.swaps))
        for first, second in self.swaps:
            print(first, second)


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
                    heap_builder_instance = BuildHeap()
                    heap_builder_instance.read_data()
                    heap_builder_instance.build_heap()
                    heap_builder_instance.print_results()
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
    # heap_builder = BuildHeap()
    # heap_builder.read_data()
    # heap_builder.build_heap()
    # heap_builder.print_results()

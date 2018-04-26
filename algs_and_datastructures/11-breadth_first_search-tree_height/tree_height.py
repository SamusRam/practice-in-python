# python3

import sys
from collections import deque
import unittest
import os


class TreeHeight:

    def __init__(self):
        # read the data
        self.n = int(sys.stdin.readline())
        self.parents = list(map(int, sys.stdin.readline().split()))

        # create adj_list
        self.adj_list = [[] for _ in range(self.n)]
        for node, parent in enumerate(self.parents):
            if parent == -1:
                self.root = node
            else:
                self.adj_list[parent].append(node)

    def get_max_height(self):
        open_nodes = deque([(self.root, 1)])
        while len(open_nodes) > 0:
            current_node = open_nodes.popleft()
            current_node_height = current_node[1]
            for child in self.adj_list[current_node[0]]:
                open_nodes.append((child, current_node_height + 1))
        return current_node_height


class Tester(unittest.TestCase):

    def test_all_scenarios(self):
        path_to_test_cases = os.path.join(os.getcwd(), 'tests')
        input_file_names = [f for f in os.listdir(path_to_test_cases)
                            if os.path.isfile(os.path.join(path_to_test_cases, f)) and f[-2:] != '.a']
        current_stdin = sys.stdin

        try:
            for file in input_file_names:
                file_path = os.path.join(path_to_test_cases, file)
                with open(file_path, 'r') as file_object:
                    sys.stdin = file_object
                    simulator_instance = TreeHeight()
                    instance_output = simulator_instance.get_max_height()
                answer_file_path = os.path.join(path_to_test_cases, file + '.a')
                with open(answer_file_path, 'r') as answer_file_object:
                    correct_output = int(answer_file_object.read().strip())
                self.assertEqual(instance_output, correct_output, 'test on file ' + file)
        finally:
            sys.stdin = current_stdin

if __name__ == '__main__':
    unittest.main()
    # tree_height = TreeHeight()
    # print(tree_height.get_max_height())

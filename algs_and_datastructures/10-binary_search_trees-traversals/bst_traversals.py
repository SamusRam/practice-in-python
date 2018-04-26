# python 3
import sys
import threading
import unittest
import os
import io
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class Traverser:

    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [-1] * self.n
        self.left = [-1] * self.n
        self.right = [-1] * self.n
        self.result = []
        for i in range(self.n):
            [self.key[i], self.left[i], self.right[i]] = map(int, sys.stdin.readline().split())

    def result_reset(self):
        self.result = []

    def get_result(self):
        return self.result

    def compute_in_order(self, node_index=0):
        if self.left[node_index] != -1:
            self.compute_in_order(self.left[node_index])
        self.result.append(self.key[node_index])
        if self.right[node_index] != -1:
            self.compute_in_order(self.right[node_index])

    def compute_in_preorder(self, node_index=0):
        self.result.append(self.key[node_index])
        if self.left[node_index] != -1:
            self.compute_in_preorder(self.left[node_index])
        if self.right[node_index] != -1:
            self.compute_in_preorder(self.right[node_index])

    def compute_in_postorder(self, node_index=0):
        if self.left[node_index] != -1:
            self.compute_in_postorder(self.left[node_index])
        if self.right[node_index] != -1:
            self.compute_in_postorder(self.right[node_index])
        self.result.append(self.key[node_index])

    def print_traversals_all(self):
        self.compute_in_order()
        print(" ".join(map(str, self.get_result())))
        self.result_reset()
        self.compute_in_preorder()
        print(" ".join(map(str, self.get_result())))
        self.result_reset()
        self.compute_in_postorder()
        print(" ".join(map(str, self.get_result())))

    def do_job(self):
        threading.Thread(target=self.print_traversals_all()).start()


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
                    worker_instance = Traverser()
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
    # worker = Traverser()
    # worker.do_job()


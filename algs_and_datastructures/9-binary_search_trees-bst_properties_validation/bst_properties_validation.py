# python 3
import sys
import threading
import unittest
import os
import io
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class BstChecker:

    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [-1] * self.n
        self.right = [-1] * self.n
        self.left = [-1] * self.n
        for i in range(self.n):
            [self.key[i], self.left[i], self.right[i]] = map(int, sys.stdin.readline().split())

    def get_tree_size(self):
        return self.n

    def check_bst_property(self, node_index=0, lower_bound=-float("inf"), upper_bound=float("inf")):
        if self.key[node_index] < lower_bound or self.key[node_index] >= upper_bound:
            return False
        else:
            left_child_check = True if self.left[node_index] == -1 \
                else self.check_bst_property(self.left[node_index], lower_bound, self.key[node_index])
            right_child_check = True if self.right[node_index] == -1 \
                else self.check_bst_property(self.right[node_index], self.key[node_index], upper_bound)
            return left_child_check and right_child_check

    def perform_check(self):
        if self.get_tree_size() == 0 or self.check_bst_property():
            print('CORRECT')
        else:
            print('INCORRECT')

    def do_job(self):
        threading.Thread(target=self.perform_check).start()


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
                    worker_instance = BstChecker()
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
    # worker = BstChecker()
    # worker.do_job()

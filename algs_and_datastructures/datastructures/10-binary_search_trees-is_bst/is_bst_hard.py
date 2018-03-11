# python 3

import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class Bst_Checker():

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


def main():
    worker = Bst_Checker()
    if worker.get_tree_size() == 0 or worker.check_bst_property():
        print('CORRECT')
    else:
        print('INCORRECT')

threading.Thread(target=main).start()


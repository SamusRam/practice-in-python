# python 3
import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class Traverser():

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


def main():
    worker = Traverser()
    worker.compute_in_order()
    print(" ".join(map(str, worker.get_result())))
    worker.result_reset()
    worker.compute_in_preorder()
    print(" ".join(map(str, worker.get_result())))
    worker.result_reset()
    worker.compute_in_postorder()
    print(" ".join(map(str, worker.get_result())))

threading.Thread(target=main).start()


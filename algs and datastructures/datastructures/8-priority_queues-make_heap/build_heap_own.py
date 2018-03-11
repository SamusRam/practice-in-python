#python3
import sys
from math import floor

class BuildHeap():

    def __init__(self):
        self._data = []
        self._swaps = []

    def read_data(self):
        n = int(sys.stdin.readline())
        self._data = [int(x) for x in sys.stdin.readline().split()]
        assert n == len(self._data)

    def heapify(self, i):
        #children
        left_child_idx = 2 * (i + 1) - 1
        right_child_idx = 2 * (i + 1)

        min_idx = i
        if left_child_idx < len(self._data) and self._data[left_child_idx] < self._data[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self._data) and self._data[right_child_idx] < self._data[min_idx]:
            min_idx = right_child_idx
        if min_idx != i:
            temp = self._data[i]
            self._data[i] = self._data[min_idx]
            self._data[min_idx] = temp
            self._swaps.append((i, min_idx))
            self.heapify(min_idx)

    def build_heap(self):
        for i in range(int(floor(len(self._data)/2)) - 1, -1, -1):
            self.heapify(i)

    def print_results(self):
        print(len(self._swaps))
        for first, second in self._swaps:
            print(first, second)

if __name__ == '__main__':
    heap_builder = BuildHeap()
    heap_builder.read_data()
    heap_builder.build_heap()
    heap_builder.print_results()
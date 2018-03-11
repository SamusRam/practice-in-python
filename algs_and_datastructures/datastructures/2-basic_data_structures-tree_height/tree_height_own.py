# python3

import sys
from collections import deque
class TreeHeight():
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parents = list(map(int, sys.stdin.readline().split()))

    def create_adj_list(self):
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


if __name__ == '__main__':
    tree_height = TreeHeight()
    tree_height.read()
    tree_height.create_adj_list()
    print(tree_height.get_max_height())
#python3

import sys

class MergeTables():

    def __init__(self):
        self.number_of_tables, self.number_of_queries = [int(x) for x in sys.stdin.readline().split()]
        self.sizes = [int(x) for x in sys.stdin.readline().split()]
        self.ranks = [1 for _ in range(self.number_of_tables)]
        self.parent = list(range(self.number_of_tables))
        self.max_size = max(self.sizes)

    def do_job(self):
        for _ in range(self.number_of_queries):
            self.process_query()

    def process_query(self):
        source, destination = [int(x) for x in sys.stdin.readline().split()]
        self.union(source - 1, destination - 1)
        print(self.max_size)


    def union(self, source, target):
        group_1 = self.find(source)
        group_2 = self.find(target)
        if group_1 != group_2:
            larger = max(group_1, group_2, key=lambda x: (self.ranks[x], x))
            smaller = min(group_1, group_2, key=lambda x: (self.ranks[x], x))
            self.parent[smaller] = larger
            self.ranks[larger] = max(self.ranks[larger], self.ranks[smaller] + 1)
            self.sizes[larger] += self.sizes[smaller]
            self.max_size = max(self.sizes[larger], self.max_size)


    def find(self, i):
        group_rep = i
        while group_rep != self.parent[group_rep]:
            group_rep = self.parent[group_rep]

        # path compression
        if i != group_rep:
            next = self.parent[i]
            current = i
            while next != group_rep:
                self.parent[current] = group_rep
                self.ranks[group_rep] = max(self.ranks[group_rep], self.ranks[current] + 1)
                current = next
                next = self.parent[current]
        return(group_rep)

    def find_rec(self, i):
        if i != self.parent[i]:
            group_rep = self.find_rec(self.parent[i])
            self.parent[i] = group_rep
            self.ranks[group_rep] = max(self.ranks[group_rep], self.ranks[i] + 1)

        return(self.parent[i])




if __name__ == '__main__':
    worker = MergeTables()
    worker.do_job()
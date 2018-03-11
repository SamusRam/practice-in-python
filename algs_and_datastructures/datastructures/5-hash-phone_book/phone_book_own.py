#python3

import sys

class DirectAddressing():

    def __init__(self):
        self.mapping = dict()
        self.phones = list()
        self.number_of_queries = int(sys.stdin.readline())

    def add(self, number, name):
        if number in self.mapping:
            # if the user was removed
            if self.mapping[number] < 0:
                self.mapping[number] = -1 * (self.mapping[number] + 1)
            self.phones[self.mapping[number]] = name
        else:
            self.mapping[number] = len(self.mapping)
            self.phones.append(name)

    def delete(self, number):
        if number in self.mapping and self.mapping[number] >= 0:
            self.mapping[number] = -1 * self.mapping[number] - 1

    def find(self, number):
        if number in self.mapping and self.mapping[number] >= 0:
            print(self.phones[self.mapping[number]])
        else:
            print('not found')

    def process_query(self):
        query_list = sys.stdin.readline().split()
        {
            'add': self.add,
            'del': self.delete,
            'find': self.find
        }[query_list[0]](*query_list[1:])

    def do_job(self):
        for _ in range(self.number_of_queries):
            self.process_query()


if __name__ == '__main__':
    worker = DirectAddressing()
    worker.do_job()

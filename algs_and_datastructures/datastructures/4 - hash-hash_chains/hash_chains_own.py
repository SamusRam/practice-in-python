#python3

import sys

class HashChain():

    class LinkedList():
        def __init__(self):
            self.length = 0
            self.head = None

        def insert(self, el):
            new_element = [el, self.head]
            self.head = new_element
            self.length += 1

        def print(self):
            next_el = self.head
            result = []
            while next_el != None:
                result.append(next_el[0])
                next_el = next_el[1]
            print(' '.join(result))

        def contains(self, el):
            return self.__contains_helping__(self.head, el)

        def __contains_helping__(self, pointer, el):
            if pointer is None:
                return False
            if pointer[0] == el:
                return True
            return self.__contains_helping__(pointer[1], el)

        def remove(self, el):
            self.head = self.__remove_rec__(self.head, el)

        def __concat_head_tail__(self, head, tail):
            head[1] = tail
            return head

        def __remove_rec__(self, head, el):
            if head == None:
                return head
            if head[0] == el:
                return head[1]
            return self.__concat_head_tail__(head, self.__remove_rec__(head[1], el))

    def __init__(self):
        self.number_of_buckets = int(sys.stdin.readline())
        self.number_of_queries = int(sys.stdin.readline())
        self.x = 263
        self.p = 1000000007
        self.hash_table = [self.LinkedList() for _ in range(self.number_of_buckets)]

    def compute_bucket_idx(self, string):
        sum = 0
        for idx, char in enumerate(string):
            sum += (ord(char) * self.x**idx)
        bucket_idx = sum % self.p % self.number_of_buckets
        return bucket_idx

    def add(self, string):
        bucket_idx = self.compute_bucket_idx(string)
        if not self.hash_table[bucket_idx].contains(string):
            self.hash_table[bucket_idx].insert(string)

    def delete(self, string):
        bucket_idx = self.compute_bucket_idx(string)
        self.hash_table[bucket_idx].remove(string)

    def find(self, string):
        bucket_idx = self.compute_bucket_idx(string)
        if self.hash_table[bucket_idx].contains(string):
            print('yes')
        else:
            print('no')

    def check(self, bucket_idx):
        self.hash_table[int(bucket_idx)].print()

    def process_line(self):
        next_line = sys.stdin.readline().split()

        {'add': self.add,
         'del': self.delete,
         'find': self.find,
         'check': self.check}[next_line[0]](next_line[1])

    def do_job(self):
        for _ in range(self.number_of_queries):
            self.process_line()


if __name__ == '__main__':
    worker = HashChain()
    worker.do_job()
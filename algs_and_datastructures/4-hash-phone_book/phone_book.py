# python3
import sys
import unittest
import os
import io


class DirectAddressing:

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
                    worker_instance = DirectAddressing()
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
    # worker = DirectAddressing()
    # worker.do_job()

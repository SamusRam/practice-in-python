# python3
import sys
import unittest
import os


def check_brackets(input_list):
    opening_brackets = {'[', '(', '{'}
    closing_brackets = {']', ')', '}'}
    brackets_stack = []
    opening_pair = {']':'[', ')':'(', '}':'{'}
    for idx, char in enumerate(input_list):
        if char in closing_brackets:
            if len(brackets_stack) == 0 or brackets_stack.pop()[0] != opening_pair[char]:
                return idx + 1
        elif char in opening_brackets:
            brackets_stack.append((char, idx + 1))
    if len(brackets_stack) == 0:
        return 'Success'
    else:
        return brackets_stack[0][1]

'''
class BasicTests(unittest.TestCase):

    def test1(self):
        self.assertEqual('Success', check_brackets(list('[]')))

    def test2(self):
        self.assertEqual('Success', check_brackets(list('{}[]')))

    def test3(self):
        self.assertEqual('Success', check_brackets(list('[()]')))

    def test4(self):
        self.assertEqual('Success', check_brackets(list('(())')))

    def test5(self):
        self.assertEqual('Success', check_brackets(list('{[]}()')))

    def test6(self):
        self.assertEqual(1, check_brackets(list('{')))

    def test7(self):
        self.assertEqual(3, check_brackets(list('{[}')))

    def test8(self):
        self.assertEqual('Success', check_brackets(list('foo(bar);')))

    def test9(self):
        self.assertEqual(10, check_brackets(list('foo(bar[i);')))

    def test10(self):
        self.assertEqual(1, check_brackets(list('}')))
'''


class Tester(unittest.TestCase):

    def test_all_scenarios(self):
        path_to_test_cases = os.path.join(os.getcwd(), 'tests')
        input_file_names = [f for f in os.listdir(path_to_test_cases)
                            if os.path.isfile(os.path.join(path_to_test_cases, f)) and f[-2:] != '.a']

        for file in input_file_names:
            file_path = os.path.join(path_to_test_cases, file)
            with open(file_path, 'r') as file_object:
                input = list(file_object.read())
            instance_output = str(check_brackets(input))
            answer_file_path = os.path.join(path_to_test_cases, file + '.a')
            with open(answer_file_path, 'r') as answer_file_object:
                correct_output = answer_file_object.read().strip()
            self.assertEqual(instance_output if instance_output != '\n' else '',
                             correct_output, 'test on file ' + file)


if __name__ == '__main__':
    unittest.main()
    # input = list(sys.stdin.read())
    # print(check_brackets(input))

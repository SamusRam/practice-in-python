# python3
import sys
# import unittest


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

if __name__ == '__main__':
    # unittest.main()
    input = list(sys.stdin.read())
    print(check_brackets(input))
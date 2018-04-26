# python 3
import sys
from collections import deque
import unittest
import os
import io


class Simulator:
    def __init__(self):
        self.max_buffer_size, self.count = map(int, sys.stdin.readline().strip().split())
        self.buffer = deque([])
        self.clock = -1
        self.idx = 0
        self.start_times = [-1 for _ in range(self.count)]

    def process_input(self):
        zero_length_count = 0
        while self.idx < self.count:
            arr_t, p_t = map(int, sys.stdin.readline().strip().split())
            if arr_t == self.clock:
                if len(self.buffer) - zero_length_count < self.max_buffer_size:
                    self.buffer.append([self.idx, arr_t, p_t])
            else:
                self.clock = arr_t
                if p_t == 0 and len(self.buffer) == 0:
                    zero_length_count += 1
                while len(self.buffer) > 0 and self.buffer[0][1] + self.buffer[0][2] <= self.clock:
                    head_idx, head_start_t, head_p_t = self.buffer.popleft()
                    if head_p_t == 0:
                        zero_length_count -= 1
                    self.start_times[head_idx] = head_start_t
                    if len(self.buffer):
                        self.buffer[0][1] = max(self.buffer[0][1], head_start_t + head_p_t)
                if len(self.buffer) - zero_length_count < self.max_buffer_size:
                    self.buffer.append([self.idx, arr_t, p_t])

            self.idx += 1
        while len(self.buffer) > 1:
            head_idx, head_start_t, head_p_t = self.buffer.popleft()
            self.start_times[head_idx] = head_start_t
            self.buffer[0][1] = max(self.buffer[0][1], head_start_t + head_p_t)
        if len(self.buffer) > 0:
            head_idx, head_start_t, head_p_t = self.buffer.popleft()
            self.start_times[head_idx] = head_start_t
        print('\n'.join(map(str, self.start_times)))


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
                    simulator_instance = Simulator()
                    simulator_instance.process_input()
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
    # simulator = Simulator()
    # simulator.process_input()

# python3
import sys
import unittest
import os
import io


class JobQueue:
    def __init__(self):
        self.number_of_threads, self.number_of_processes = [int(x) for x in sys.stdin.readline().split()]
        self.job_queue = [int(x) for x in sys.stdin.readline().split()]
        self.results = [(-1, -1) for _ in range(self.number_of_processes)]
        self.data = [(idx, 0) for idx in range(self.number_of_threads)]

    def process(self):
        for next_job_idx in range(self.number_of_processes):
            next_free_thread = self.data[0]
            self.results[next_job_idx] = next_free_thread
            next_job_duration = self.job_queue[next_job_idx]
            self.data[0] = (self.data[0][0], self.data[0][1] + next_job_duration)
            self.heapify(0)

    def heapify(self, i):
        # children
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        min_idx = i
        if left_child_idx < len(self.data) and (self.data[left_child_idx][1] < self.data[min_idx][1] or
                                                     (self.data[left_child_idx][1] == self.data[min_idx][1] and
                                                              self.data[left_child_idx][0] < self.data[min_idx][0])):
            min_idx = left_child_idx
        if right_child_idx < len(self.data) and (self.data[right_child_idx][1] < self.data[min_idx][1] or
                                                     (self.data[right_child_idx][1] == self.data[min_idx][1] and
                                                              self.data[right_child_idx][0] < self.data[min_idx][0])):
            min_idx = right_child_idx
        if min_idx != i:
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.heapify(min_idx)

    def print_results(self):
        for thread, start_time in self.results:
            print(thread, start_time)


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
                    job_queue_instance = JobQueue()
                    job_queue_instance.process()
                    job_queue_instance.print_results()
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
    # job_queue = JobQueue()
    # job_queue.process()
    # job_queue.print_results()

#python 3
import sys
from collections import deque

class Simulator():
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
        print('\n'.join(map(str,self.start_times)))


if __name__ == '__main__':
    simulator = Simulator()
    simulator.process_input()
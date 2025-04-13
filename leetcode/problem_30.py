from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        words_counts = Counter(words)
        substring_indices = []
    
        for possible_recomputation_offset in range(word_len):
            window_start_index = possible_recomputation_offset
            window_end_index = possible_recomputation_offset
            current_window_counts = Counter()
            while window_end_index + word_len <= len(s):
                next_included_word = s[window_end_index: window_end_index + word_len]
                window_end_index += word_len
                if next_included_word in words_counts:
                    current_window_counts[next_included_word] += 1
                    while current_window_counts[next_included_word] > words_counts[next_included_word]:
                        current_window_counts[s[window_start_index: window_start_index + word_len]] -= 1
                        window_start_index += word_len
                    if current_window_counts == words_counts:
                        substring_indices.append(window_start_index)
                else:
                    window_start_index = window_end_index
                    current_window_counts = Counter()
        return substring_indices
            

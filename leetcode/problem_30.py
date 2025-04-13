from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        number_of_words = len(words)
        permutation_len = word_len * number_of_words
        words_counts = Counter(words)
        substring_indices = []
        for starting_index in range(len(s) - permutation_len + 1):
            current_window = s[starting_index:starting_index + permutation_len]
            current_window_counts = Counter(current_window[i: i + word_len] for i in range(0, permutation_len, word_len))
            if current_window_counts == words_counts:
                substring_indices.append(starting_index)
        return substring_indices

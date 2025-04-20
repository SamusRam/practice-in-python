class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 1
        left_i = 0
        right_i = 1
        present_chars = {s[0]}
        while right_i < len(s):
            while s[right_i] in present_chars:
                present_chars.remove(s[left_i])
                left_i += 1
            present_chars.add(s[right_i])
            right_i += 1
            max_len = max(max_len, right_i - left_i)
            
        return max_len
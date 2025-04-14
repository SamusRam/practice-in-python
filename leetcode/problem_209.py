class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start_i = 0
        end_i = 0
        current_sum = 0
        best_len = float('inf')
        while end_i < len(nums):
            current_sum += nums[end_i]
            while current_sum - nums[start_i] >= target:
                current_sum -= nums[start_i]
                start_i += 1
            if current_sum >= target:   
                best_len = min(end_i - start_i + 1, best_len)
            end_i += 1
        return 0 if best_len == float('inf') else best_len
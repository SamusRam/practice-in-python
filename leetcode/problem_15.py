class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        tuples = set()
        for first_index in range(len(nums) - 2):
            left_index = first_index + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                current_tuple = (nums[first_index], nums[left_index], nums[right_index])
                current_sum = sum(current_tuple)
                if current_sum == 0:
                    tuples.add(current_tuple)
                    left_index += 1
                    right_index -= 1
                elif current_sum < 0:
                    left_index += 1
                else:
                    right_index -= 1
        return [list(t) for t in tuples]
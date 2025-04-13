class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for first_index in range(len(nums) - 2):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                # triplets with such first index have been checked
                continue
            left_index = first_index + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                current_tuple = [nums[first_index], nums[left_index], nums[right_index]]
                current_sum = sum(current_tuple)
                if current_sum == 0:
                    triplets.append(current_tuple)
                    left_index += 1
                    right_index -= 1
                    while left_index < right_index and nums[left_index - 1] == nums[left_index]:
                        left_index += 1
                    while right_index > left_index and nums[right_index + 1] == nums[right_index]:
                        right_index -= 1
                elif current_sum < 0: 
                    left_index += 1
                else:
                    right_index -= 1
        return triplets
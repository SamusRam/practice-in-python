class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_pointer_to_unique = 0
        faster_pointer = 0
        while faster_pointer < len(nums):
            while faster_pointer < len(nums) and nums[last_pointer_to_unique] == nums[faster_pointer]:
                faster_pointer += 1
            last_pointer_to_unique += 1
            if last_pointer_to_unique < len(nums) and nums[last_pointer_to_unique] <= nums[last_pointer_to_unique - 1]:
                if faster_pointer < len(nums):
                    nums[last_pointer_to_unique] = nums[faster_pointer]
                else:
                    last_pointer_to_unique -= 1
        return last_pointer_to_unique + 1
        
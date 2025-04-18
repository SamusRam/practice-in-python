class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_i = 0
        for read_i in range(1, len(nums)):
            if nums[read_i] > nums[write_i] or write_i == 0 or nums[write_i - 1] != nums[write_i]:
                write_i += 1
                nums[write_i] = nums[read_i]
        return write_i + 1
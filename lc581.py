class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start_index, end_index = None, None
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start_index = i
                break
        if start_index is None:
            return 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != sorted_nums[i]:
                end_index = i
                break
        return end_index - start_index + 1
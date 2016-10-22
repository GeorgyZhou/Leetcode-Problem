class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 2:
            return nums[0]
        nums.sort()
        print
        left, right = 0, len(nums) - 1
        while left < right:
            if left == right - 1:
                return nums[left]
            middle = left + (right - left) / 2
            if nums[middle] <= middle:
                right = middle
            else:
                left = middle
                
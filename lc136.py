class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        res = nums[0]
        for i in xrange(1, n):
            res ^= nums[i]
        return res
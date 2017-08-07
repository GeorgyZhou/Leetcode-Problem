class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s
        
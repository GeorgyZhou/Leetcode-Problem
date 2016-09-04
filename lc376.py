class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        f = d = 1
        for i in xrange(1, n):
            if nums[i] > nums[i-1]:
                f = d + 1
            elif nums[i] < nums[i-1]:
                d = f + 1
        return max(d, f)
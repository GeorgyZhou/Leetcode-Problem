class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return [[]]
        if n == 1:
            return [nums]
        ret = []
        for i in xrange(n):
            for per in self.permute(nums[0:i] + nums[i+1:n]):
                per.append(nums[i])
                ret.append(per)
        return ret

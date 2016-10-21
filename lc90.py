class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return [[]]
        elif n == 1:
            return [[], [nums[0]]]
        nums.sort()
        ret = [[]]
        size = 0
        for i in xrange(n):
            start = size if i > 0 and nums[i] == nums[i-1] else 0
            size = len(ret)
            for j in xrange(start, size):
                ret.append(ret[j] + [nums[i]])
        return ret
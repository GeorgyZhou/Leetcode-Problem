class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = 1
        n = len(nums)
        zeros = []
        for i in xrange(n):
            if nums[i] == 0:
                zeros.append(i)
            else:
                products *= nums[i]
        if len(zeros) > 1:
            return [0 for _ in xrange(n)]
        if len(zeros) == 1:
            return [(0 if i != zeros[0] else products) for i in xrange(n)]
        ret = []
        for i in xrange(n):
            ret.append(products / nums[i])
        return ret
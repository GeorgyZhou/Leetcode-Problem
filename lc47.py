class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return [[]]
        if n == 1:
            return [nums]
        nums.sort()
        ret = []
        last = None
        for i in xrange(n):
            if last != nums[i]:
                for per in self.permuteUnique(nums[0:i] + nums[i+1:n]):
                    per.append(nums[i])
                    ret.append(per)
                last = nums[i]
        return ret
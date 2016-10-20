class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n <= 1:
            return [[]] + [[i] for i in nums]
        last = self.subsets(nums[:-1])
        now = []
        for i in last:
            now.append(i + [nums[-1]])
        now += last    
        return now
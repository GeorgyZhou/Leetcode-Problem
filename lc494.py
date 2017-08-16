class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.mem = dict()
        a = self.dfs(nums, 0, S)
        return a
        
    
    def dfs(self, nums, start, s):
        if (start, s) in self.mem:
            return self.mem[(start, s)]
        if start == len(nums) - 1:
            if s - nums[start] == 0:
                self.mem[(start, s)] = self.mem.get((start, s), 0) + 1
            if s + nums[start] == 0:
                self.mem[(start, s)] = self.mem.get((start, s), 0) + 1
            if s + nums[start] != 0 and s - nums[start] != 0:
                self.mem[(start, s)] = 0
            return self.mem[(start, s)]
        addon = self.dfs(nums, start + 1, s - nums[start])
        minus = self.dfs(nums, start + 1, s + nums[start])
        self.mem[(start, s)] = addon + minus
        return self.mem[(start, s)]
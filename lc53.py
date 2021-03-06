class Solution(object):
    def maxSubArray(self, nums):
        import sys
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0] 
        dp = [nums[0]] + [-sys.maxint-1 for _ in xrange(n-1)]
        for i in xrange(1, n):
            dp[i] = nums[i] + dp[i-1] if dp[i-1] > 0 else nums[i]
        max_num = -sys.maxint - 1
        for i in xrange(0, n):
            if dp[i] > max_num:
                max_num = dp[i]
        return max_num
            

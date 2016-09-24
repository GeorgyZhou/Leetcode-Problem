class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0, nums[0]]+[0 for _ in xrange(n-1)]
        for i in xrange(1, n):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        return dp[n]

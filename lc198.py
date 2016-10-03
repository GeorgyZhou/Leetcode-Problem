class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0, nums[0]]+[0 for _ in xrange(n-2)]
        for i in xrange(1, n-1):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        res = dp[n-1]

        dp = [0, 0]+[0 for _ in xrange(n-1)]
        for i in xrange(1, n):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i])
        return max(res,dp[n])

class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return 0
        dp = [nums[0]] + [None for _ in xrange(n-1)]
        dp1 = [nums[0]] + [None for _ in xrange(n-1)]
        parent = dict()
        max_prod = nums[0]
        for i in xrange(1, n):
            dp[i] = max(dp[i-1]*nums[i], nums[i], dp1[i-1]*nums[i])
            dp1[i] = min(dp[i-1]*nums[i], nums[i], dp1[i-1]*nums[i])
            if dp[i] > max_prod:
                max_prod = dp[i]
        return max_prod


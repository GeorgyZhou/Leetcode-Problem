class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l1 = l2 = l3 = 0
        dp = [1] + [0 for _ in xrange(n - 1)]
        for i in xrange(1, n):
            dp[i] = min(dp[l1] * 2, dp[l2] * 3, dp[l3] * 5)
            if dp[i] == dp[l1] * 2:
                l1 += 1
            if dp[i] == dp[l2] * 3:
                l2 += 1
            if dp[i] == dp[l3] * 5:
                l3 += 1
        print dp
        return dp[n-1]

solution = Solution()
print solution.nthUglyNumber(10)
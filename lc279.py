class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import sys
        if n < 4:
            return n
        dp = [sys.maxint for _ in xrange(n + 1)]
        root = 1
        for i in xrange(1, n+1):
            if i == root * root:
                dp[i] = 1
            elif i == root * root + 2 * root + 1:
                dp[i] = 1
                root += 1
            else:
                for j in xrange(root + 1):
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
        print dp
        return dp[n]

solution = Solution()
print solution.numSquares(12)
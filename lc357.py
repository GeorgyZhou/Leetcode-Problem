class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = [1, 10] + [None for _ in xrange(9)]
        for i in xrange(2, min(10, n)+1, 1):
            current = 9
            for j in xrange(11-i,10,1):
                current *= j
            dp[i] = dp[i-1] + current
        return dp[min(10, n)]


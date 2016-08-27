class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        k = len(primes)
        list = [0 for _ in xrange(k)]
        dp = [1] + [0 for _ in xrange(n - 1)]
        for i in xrange(1, n):
            dp[i] = min(dp[list[j]] * primes[j] for j in xrange(k))
            for j in xrange(k):
                if dp[i] == dp[list[j]] * primes[j]:
                    list[j] += 1
        print dp
        return dp[n-1]

solution = Solution()
print solution.nthSuperUglyNumber(2, [2, 3, 5])
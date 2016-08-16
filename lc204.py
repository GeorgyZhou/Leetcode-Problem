class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [True for _ in xrange(0, n)]
        p = 2
        while p * p < n:
            if not isPrime[p]:
                p += 1
                continue
            k = p * p
            while k < n:
                isPrime[k] = False
                k += p
            p += 1
        count = 0
        for i in xrange(2, n):
            if isPrime[i]:
                count += 1
        return count

solution = Solution()
print solution.countPrimes(13)

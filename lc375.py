class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cost = [[0] * (n + 1) for i in xrange(n + 1)]
        for low in xrange(n,  0, -1):
            for high in xrange(low+1, n+1, 1):
                cost[low][high] = min(x + max(cost[low][x-1], cost[x+1][high]) for x in range(low, high))

        return cost[1][n]

solution = Solution()
solution.getMoneyAmount(20)
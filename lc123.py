class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        result = 0
        max1 = [0 for _ in xrange(n)]
        max2 = [0 for _ in xrange(n)]
        i, j = 1, n - 2
        local_max = prices[n-1]
        local_min = prices[0]
        while i < n and j >= 0:
            max1[j] = max(max1[j + 1], local_max - prices[j])
            local_max = max(local_max, prices[j])
            max2[i] = max(max2[i - 1], prices[i] - local_min)
            local_min = min(local_min, prices[i])
            j -= 1
            i += 1

        for i in xrange(n):
            result = max(result, max1[i] + max2[i])
        return result


solution = Solution()
print solution.maxProfit([1,2,3,4,5,6])
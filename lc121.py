class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxpro = low = high = 0
        for i in xrange(1, len(prices)):
            high = i
            if prices[i - 1] < prices[low] and i - 1 < high:
                low = i - 1
            maxpro = max(prices[high] - prices[low], maxpro)
        return maxpro


solution = Solution()
print solution.maxProfit([7, 1, 5, 3, 6, 4])
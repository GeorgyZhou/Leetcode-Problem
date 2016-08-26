class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in xrange(len(prices) - 1):
            total += max(prices[i+1] - prices[i], 0)
        return total
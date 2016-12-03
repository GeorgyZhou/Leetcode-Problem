class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        import sys
        state1 = [0 for _ in range(n)] # buy
        state2 = [0 for _ in range(n)] # sell
        state3 = [0 for _ in range(n)] # rest
        state1[0], state2[0], state3[0] = -prices[0], -sys.maxint - 1, 0
        for i in xrange(1, n):
            state2[i] = state1[i-1] + prices[i]
            state3[i] = max(state3[i-1], state2[i-1])
            state1[i] = max(state1[i-1], state3[i-1] - prices[i])
        return max(state2[-1], state3[-1])
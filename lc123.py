class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        maxpro = low1 = high1 = high2 = low2= 0
        for i in xrange(0, len(prices)):
            middle = i
            max1 = max2 = 0
        return maxpro

solution = Solution()
print solution.maxProfit([1,2,3,4,5,6])
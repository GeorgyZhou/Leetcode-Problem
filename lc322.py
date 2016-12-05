class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        if amount <= 0:
            return -1 if amount < 0 else 0
        dp = [sys.maxint for _ in range(amount+1)]
        dp[0] = 0
        for i in coins:
            if i <= amount:
                dp[i] = 1
        for i in range(1, amount+1):
            for num in coins:
                if i - num >= 0 and dp[i-num] != -1:
                    dp[i] = min(dp[i], dp[i-num]+1)
            if dp[i] == sys.maxint:
                dp[i] = -1
        return dp[amount]
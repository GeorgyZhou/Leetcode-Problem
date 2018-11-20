class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] * (n+2)] * (n+2)
        for size in range(1, n + 1):
            for index in range(n - size + 1):
                if (size - 1 - n) % 2 == 1:
                    dp[index+1][index + size] = max(piles[index+size-1] + dp[index][index+size-2],
                                                      piles[index] + dp[index+1][index+size-1])
                else:
                    dp[index+1][index + size] = min(-piles[index+size-1] + dp[index][index+size-2],
                                                      -piles[index] + dp[index+1][index+size-1])
        return dp[0][n] > 0

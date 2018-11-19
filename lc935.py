class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        dp = [1 for _ in range(10)]
        next_dp = [1 for _ in range(10)]
        last = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        for i in range(1, N):
            for j in range(10):
                next_dp[j] = sum(dp[k] for k in last[j])
            for j in range(10):
                dp[j] = next_dp[j] % (10**9 + 7)
        return sum(dp) % (10**9 + 7)

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        import sys
        n = len(triangle)
        if n <= 1:
            return triangle[0][0] if n == 1 else 0
        ret = sys.maxint
        dp = [None for _ in range(n)]
        new_dp = [None for _ in range(n)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    new_dp[j] = dp[0] + triangle[i][j]
                elif j == i:
                    new_dp[j] = dp[i-1] + triangle[i][j]
                else:
                    new_dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            for j in range(i+1):
                dp[j] = new_dp[j]
        return min(dp)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res  =  0
        m, n = len(matrix), len(matrix[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = (i+1,j+1) if matrix[i][j] == 0 else (i,j)
                    res = max(res, (i - dp[i][j][0] + 1) * (j - dp[i][j][1] + 1))
                elif i == 0:
                    if matrix[i][j] == 0:
                        dp[i][j] = (i+1, j+1)
                    elif matrix[i][j-1] == 0:
                        dp[i][j] = (i, j)
                    else:
                        dp[i][j] = (i, dp[i][j-1][1])
                    res = max(res, (i - dp[i][j][0] + 1) * (j - dp[i][j][1] + 1))
                elif j == 0:
                    if matrix[i][j] == 0:
                        dp[i][j] = (i+1, j+1)
                    elif matrix[i-1][j] == 0:
                        dp[i][j] = (i, j)
                    else:
                        dp[i][j] = (dp[i-1][j][0], j)
                    res = max(res, (i - dp[i][j][0] + 1) * (j - dp[i][j][1] + 1))
                else:
                    if matrix[i][j] == 0:
                        dp[i][j] = (i+1, j+1)
                    elif matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
                        dp[i][j] = (i, j)
                    elif matrix[i-1][j] == 0:
                        dp[i][j] = (i, dp[i][j-1][1])
                    elif matrix[i][j-1] == 0:
                        dp[i][j] = (dp[i-1][j][0], j)
                    else:
                        dp[i][j] = (max(dp[i][j-1][0], dp[i-1][j][0]), max(dp[i][j-1][1], dp[i-1][j][1]))
                    res = max(res, (i - dp[i][j][0] + 1) * (j - dp[i][j][1] + 1))
        for i in range(m):
            print dp[i]
        for i in range(m):
            print matrix[i]
        print dp
        return res

s = Solution()
print s.maximalRectangle([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])
        
        
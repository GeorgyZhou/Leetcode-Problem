class Solution(object):
    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        if n1 == 0:
            return n2
        elif n2 == 0:
            return n1
        dp = [[0 for _ in xrange(n2 + 1)] for _ in xrange(n1 + 1)]
        for i in xrange(n2+1):
            dp[0][i] = i
        for j in xrange(n1+1):
            dp[j][0] = j
        for i in xrange(n1):
            for j in xrange(n2):
                # they are the same, no operation
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # dp[i][j] = dp[i-1][j-1] + 1 for change i, j += 1
                    # dp[i][j] = dp[i-1][j] + 1 for delete word1[i] from word1 i += 1
                    # dp[i][j] = dp[i][j-1] + 1 for insert word2[j] to word1 at i+1 j += 1
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    #if dp[i+1][j+1] == dp[i][j] + 1:
                    #    i += 1
                    #    j += 1
                    #elif dp[i+1][j+1] == dp[i][j+1] + 1:
                    #    i += 1
                    #elif dp[i+1][j+1] == dp[i+1][j] + 1:
                    #    j += 1
        return dp[n1][n2]

s = Solution()
s.minDistance('13','3')

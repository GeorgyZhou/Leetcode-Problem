class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        if l == 0:
            return True
        dp = [[None for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m+1):
            for j in xrange(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[m][n]
                
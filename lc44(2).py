class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens = len(s)
        if len(p) - p.count('*') > lens:
            return False
        dp = [True] + [False] * lens
        for i in p:
            if i != '*':
                for j in range(lens-1, -1, -1):
                    dp[j+1] = dp[j] and (s[j] == i or i == '?')
            else:
                for j in xrange(lens):
                    dp[j+1] = dp[j] or dp[j+1]
            dp[0] = dp[0] and i == '*'
        return dp[lens]

solution = Solution()
print solution.isMatch('aa','aa')
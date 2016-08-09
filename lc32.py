class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # recording the result of longestValidParentheses ending at s[i]
        dp = [0 for i in xrange(len(s))]
        res = 0
        for i in xrange(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(' and dp[i-1] > 0:
                    dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
                res = max(res, dp[i])
        print res
        return res


solution = Solution()
solution.longestValidParentheses(')(')
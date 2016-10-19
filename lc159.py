class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [(0, None, None) for _ in xrange(n+1)]
        dic = dict()
        for i in xrange(1,n+1):
            if dp[i-1][1] == s[i-1] or dp[i-1][2] == s[i-1]:
                dp[i] = (dp[i-1][0]+1, dp[i-1][1], dp[i-1][2])
            elif dp[i-1][1] is None:
                dp[i] = (dp[i-1][0]+1, s[i-1], dp[i-1][2])
            elif dp[i-1][2] is None:
                dp[i] = (dp[i-1][0]+1, dp[i-1][1], s[i-1])
            else:
                if s[i-2] == dp[i-1][1]:
                    dp[i] = (i - 1 - dic[dp[i-1][2]], dp[i-1][1], s[i-1])
                else:
                    dp[i] = (i - 1 - dic[dp[i-1][1]], dp[i-1][2], s[i-1])
            dic[s[i-1]] = i-1
            
        ret = 0
        for i in xrange(1, n+1):
            ret = max(ret, dp[i][0])
        return ret    
                    
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False
        l = len(s)
        self.words = dict()
        self.dp = [[None for _ in xrange(l+1)] for _ in xrange(l+1)]
        for i in xrange(l+1):
            self.dp[i][i] = True
        for word in wordDict:
            self.words[word] = 1
        return self.ok(s, 0, l)

    def ok(self, s, i, j):
        if self.dp[i][j] != None:
            return self.dp[i][j]
        if s[i:j] in self.words:
            self.dp[i][j] = True
        elif i + 1 == j:
            self.dp[i][j] = False
        else:
            for k in xrange(i+1,j):
                self.dp[i][j] = self.ok(s,i,k) and self.ok(s, k,j)
                if self.dp[i][j]:
                    return True
            self.dp[i][j] = False
        return self.dp[i][j]


sol = Solution()
print sol.wordBreak("a",
            ["a", 'code'])
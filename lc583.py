class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.dp = dict()
        lcs = self.lcs(word1, word2, len(word1), len(word2))
        return len(word1) + len(word2) - 2 * lcs 
    
    def lcs(self, s1, s2, m, n):
        if n <= 0 or m <= 0:
            return 0
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        if s1[m-1] == s2[n-1]:
            self.dp[(m, n)] = 1 + self.lcs(s1, s2, m-1, n-1)
        else:
            self.dp[(m, n)] = max(self.lcs(s1, s2, m-1, n) , self.lcs(s1, s2, m, n-1))
        return self.dp[(m, n)] 
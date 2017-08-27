    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zero_count, one_count = self.getCounts(s)
            for i in range(m, zero_count-1, -1):
                for j in range(n, one_count-1, -1):
                    dp[i][j] = max(1+dp[i-zero_count][j-one_count], dp[i][j])
        return dp[m][n]
        
    
    def getCounts(self, s):
        zeros = 0
        for char in s:
            if char == '0':
                zeros += 1
        return zeros, len(s) - zeros
class Solution(object):
    def isMatch(self, s, p):
        if s == '' or p == '':
            return False
        lenS, lenP = len(s), len(p)
        dp = [[False] * (lenP + 1)  for i in range(lenS + 1)]
        dp[0][0] = True
        first_is_located = False
        for i in range(lenS):
            for j in range(lenP):
                if '*' == p[j]:
                    if p[j-1] == s[i] or p[j-1] == '.':
                        # dp[i][j] = dp[i][j-2] for empty
                        # dp[i][j] = dp[i-1][j] for duplicate (a* more than or equal to 2)
                        # dp[i][j] = dp[i][j-1] for single
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i][j + 1] or dp[i + 1][j]
                    elif p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                        if not first_is_located:
                            dp[i][j+1] = True
                elif s[i] == p[j] or '.' == p[j]:
                    first_is_located = True
                    dp[i + 1][j + 1] = dp[i][j]
        return dp[lenS][lenP]

if __name__ == '__main__':
    solution = Solution()
    while(1):
        s = raw_input()
        p = raw_input()
        print solution.isMatch(s,p)


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        count = 0
        res = []
        S = S.upper()
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            res.append(S[i])
            count += 1
            if count == K:
                count = 0
                res.append('-')
        if len(res) > 0 and res[-1] == '-':
            res.pop()
        res.reverse()
        return ''.join(res)
            
            
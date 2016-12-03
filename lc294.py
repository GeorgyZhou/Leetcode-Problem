class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 2:
            return False
        chars = [c for c in s]
        def rec(chars):
            for i in range(1, n):
                if chars[i] == '+' and chars[i-1] == '+':
                    chars[i], chars[i-1] = '-', '-'
                    res = rec(chars)
                    chars[i], chars[i - 1] = '+', '+'
                    if not res:
                        return True
            return False
        return rec(chars)
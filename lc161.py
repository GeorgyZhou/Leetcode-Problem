class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        if abs(ls - lt) >= 2:
            return False
        flag = True
        i, j = 0, 0
        while i < ls and j < lt:
            if s[i] != t[j] and ls == lt and flag:
                flag = False
                i += 1
                j += 1
            elif s[i] != t[j] and ls < lt and flag:
                flag = False
                j += 1
            elif s[i] != t[j] and ls > lt and flag:
                flag = False
                i += 1
            elif s[i] != t[j] and not flag:
                return False
            elif s[i] == t[j]:
                i += 1
                j += 1
        if i < ls:
            return flag
        if j < lt:
            return flag
        return not flag

                

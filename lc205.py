class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        if ls != lt: return False
        sdic = dict()
        tdic = dict()
        for i in xrange(ls):
            if s[i] in sdic:
                if t[i] != sdic[s[i]]: return False
            else:
                sdic[s[i]] = t[i]
            if t[i] in tdic:
                if s[i] != tdic[t[i]]: return False
            else:
                tdic[t[i]] = s[i]
        return True
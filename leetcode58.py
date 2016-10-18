class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        start = -1
        ret = 0
        for i in xrange(n):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                ret = i - start
            else:
                start = i
        return ret
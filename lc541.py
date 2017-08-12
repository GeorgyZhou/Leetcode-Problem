class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = ""
        for i in range(0, len(s), 2*k):
            rev = s[i:i+k]
            rev = rev[::-1]
            ret += rev + s[i+k: i+2*k]
        return ret
        
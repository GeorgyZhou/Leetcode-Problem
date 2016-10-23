class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n > 0:
            cur = (n-1) % 26
            ret.append(chr(ord('A') + cur))
            n = (n-1) / 26
        ret.reverse()
        return ''.join(ret)
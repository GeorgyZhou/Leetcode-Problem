class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        for i in xrange(1, n/2+1):
            if n % i == 0 and str[0:i] * (n/i) == str:
                return True
        return False
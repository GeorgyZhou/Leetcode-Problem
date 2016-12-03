class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from math import log10
        if n <= 1:
            return n == 1
        return int(log10(n)/log10(3)) == log10(n)/log10(3)
            
        
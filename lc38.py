class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = 1
        for i in xrange(n):
            for
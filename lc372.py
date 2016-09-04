class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        last_digit = b[-1]
        del b[-1]
        return (Solution.normalPow(self, Solution.superPow(self, a, b), 10) * Solution.normalPow(self, a, last_digit)) % 1337


    def normalPow(self, a, k):
        base = 1337
        res = 1
        a %= base
        for i in xrange(k):
            res = (res * a) % base
        return res
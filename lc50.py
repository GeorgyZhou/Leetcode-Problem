class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True
        if n == 1:
            return x
        elif n < 0:
            n = -n
            flag = False
        elif n == 0:
            return 1
        if n % 2 == 0:
            ret = self.myPow(x, n/2)
            ret = ret * ret
        else:
            ret = self.myPow(x, n/2)
            ret = ret * ret * x
        if flag:
            return ret
        else:
            return 1.0 / float(ret)

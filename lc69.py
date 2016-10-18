class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left, right = 1, x
        while left < right-1:
            mid = left + (right - left) / 2
            if mid**2 < x:
                left = mid
            elif mid**2 > x:
                right = mid
            else:
                return mid
        return left
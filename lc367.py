class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 4:
            return True if num == 4 or num == 1 or num == 0 else False
        left, right = 1, num / 2
        while left <= right:
            mid = left + (right - left) / 2
            res = mid * mid
            if res == num:
                return True
            elif res > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
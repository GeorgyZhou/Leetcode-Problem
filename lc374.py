# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) / 2
            is_bad = guess(mid + 1)
            if is_bad == 0:
                return mid + 1
            elif is_bad == 1:
                left = mid + 1
            else:
                right = mid - 1
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version == 1

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) / 2
            is_bad = isBadVersion(mid + 1)
            if is_bad:
                if mid == 0:
                    return mid + 1
                last_bad = isBadVersion(mid)
                if not last_bad:
                    return mid + 1
                else:
                    right = mid - 1
            else:
                left = mid + 1
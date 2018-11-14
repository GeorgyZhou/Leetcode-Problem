class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        is_increasing = None
        for i in range(1, len(A)):
            if is_increasing is True and A[i] < A[i-1]:
                return False
            if is_increasing is False and A[i] > A[i-1]:
                return False
            if is_increasing is None and A[i] != A[i-1]:
                is_increasing = (A[i] > A[i-1])
        return True

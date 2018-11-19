class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        is_increasing = True
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                if is_increasing:
                    if i != 1:
                        is_increasing = False
                        continue
                    return False
                else:
                    continue
            elif A[i] > A[i - 1] and is_increasing:
                continue
            else:
                return False
        return not is_increasing

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] % 2 != 0:
                self.swap(A, left, right)
            if A[right] % 2 == 0:
                self.swap(A, left, right)
            if A[left] % 2 == 0:
                left += 1
            if A[right] % 2 != 0:
                right -= 1
        return A

    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

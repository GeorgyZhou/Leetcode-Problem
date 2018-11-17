class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return [[]]
        m, n = len(A), len(A[0])
        return [[A[r][c] for r in range(m)] for c in range(n)]

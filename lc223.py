class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        bx, by = max(A, E), max(B, F)
        tx, ty = min(C, G), min(D, H)
        return (C-A) * (D-B) + (G-E) * (H-F) - max((tx - bx), 0) * max((ty - by), 0)
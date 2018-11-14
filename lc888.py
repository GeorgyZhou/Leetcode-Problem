class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        sum_b = sum(B)
        target = (sum_a + sum_b) / 2
        diff = target - sum_b
        set_a = set(A)
        for b in B:
            if b + diff in set_a:
                return [b + diff, b]

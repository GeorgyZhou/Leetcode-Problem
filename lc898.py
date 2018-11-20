class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        for x in A:
            cur = {x | y for y in cur} | {x}
            res |= cur
        return len(res)

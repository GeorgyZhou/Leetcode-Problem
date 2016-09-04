class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        elif k == 1 and 1 <= n <= 9:
            return [[n]]

        ret = []
        for i in xrange(1,10):
            for ans in Solution.combinationSum(self, k-1, n-i , i+1):
                ans.append(i)
                ret.append(ans)
        return ret

    def combinationSum(self, k, n, start):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        elif k == 1 and 1 <= n <= 9 and n >= start:
            return [[n]]

        ret = []
        for i in xrange(start, 10):
            for ans in Solution.combinationSum(self, k-1, n-i, i+1):
                ans.append(i)
                ret.append(ans)
        return ret

solution = Solution()
print solution.combinationSum3(8, 36)
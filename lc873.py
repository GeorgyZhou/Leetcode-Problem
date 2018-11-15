import collections

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        dp = {}
        index = {val: i for i, val in enumerate(A)}
        ans = 0
        for i, val in enumerate(A):
            for j in range(i):
                k = val - A[j]
                if k in index and index[k] < j:
                    cand = dp[j, i] = dp.get((index[k], j), 2) + 1
                    ans = max(ans, cand)
        return ans

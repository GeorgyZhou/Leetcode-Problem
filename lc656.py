class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A or A[-1] == -1:
            return []
        n = len(A)
        dp = [(None, None) for _ in range(n)]
        dp[n-1] = (A[n-1], None)
        for i in xrange(n-2, -1, -1):
            if A[i] == -1:
                continue
            for j in range(i+1, min(i+B+1, n)):
                if dp[j][0] is None:
                    continue
                if A[j] != -1 and dp[i][0] is None or dp[j][0] + A[i] < dp[i][0]:
                    dp[i] = (dp[j][0] + A[i], j)
            if dp[i][0] is None:
                return []
        ret = []
        i = 0
        while i is not None:
            ret.append(i+1)
            i = dp[i][1]
        return ret
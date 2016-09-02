class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        if n < 10:
            return [i+1 for i in xrange(n)]
        for i in xrange(1, 10, 1):
            Solution.dfs(self, n, i, ret)
        return ret

    def dfs(self, n, cur, ret):
        if cur > n:
            return
        else:
            ret.append(cur)
            for i in xrange(10):
                if cur * 10 + i > n:
                    return
                Solution.dfs(self, n, cur * 10 + i, ret)


s = Solution()
print s.lexicalOrder(13)

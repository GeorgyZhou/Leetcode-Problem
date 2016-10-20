class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k <= 0 or k > n:
            return []
        if k == 1:
            return [[i] for i in xrange(1,n+1)]
        if k == n:
            return [range(1,n+1)]
        else:
            include_n = self.combine(n-1, k-1)
            exclude_n = self.combine(n-1, k)
            for ls in include_n:
                ls.append(n)
            exclude_n += include_n
        return exclude_n
        
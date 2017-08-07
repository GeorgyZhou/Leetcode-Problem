class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        moduler = 10 ** 9 + 7
        self.dp = dict()
        count = self.rec(m, n, N, i, j)
        return count % moduler
    
    def rec(self, m, n, N, i, j):
        if (i, j, N) in self.dp:
            return self.dp[(i, j, N)]
        count = 0
        if N == 0:
            return 0
        if j == 0:
            count += 1
        if j == n - 1:
            count += 1
        if i == 0:
            count += 1
        if i == m - 1:
            count += 1
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n:
                count += self.rec(m, n, N-1, x, y)
        self.dp[(i, j, N)] = count
        return count
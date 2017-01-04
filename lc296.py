class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        x, y = [], []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        ret = 0
        i, j = 0, len(x)-1
        while i < j:
            ret += (x[j] - x[i])
            j -= 1
            i += 1
        i, j = 0, len(y)-1
        while i < j:
            ret += (y[j] - y[i])
            i += 1
            j -= 1
        return ret
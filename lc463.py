class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ret, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                        if 0 <= x < m and 0 <= y < n:
                            if grid[x][y] == 0:
                                ret += 1
                        else:
                            ret += 1
        return ret
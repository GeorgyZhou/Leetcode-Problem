class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ret = 0
        colhits = [0 for _ in xrange(n)]
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == "W":
                    rowhits = 0
                    k = j
                    while k < n and grid[i][k] != "W" :
                        rowhits += 1 if grid[i][k] == "E" else 0
                        k += 1
                if i == 0 or grid[i-1][j] == "W":
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != "W":
                        colhits[j] += 1 if grid[k][j] == "E" else 0
                        k += 1
                if grid[i][j] == "0":
                    ret = max(ret, colhits[j] + rowhits)
        return ret
                    
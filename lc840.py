class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m <= 2 or n <= 2:
            return 0
        count = 0
        for i in xrange(1, m-1):
            for j in xrange(1, n-1):
                if self.is_magic_center(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                                        grid[i][j-1], grid[i][j], grid[i][j+1],
                                        grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]):
                    count += 1
        return count

    def is_magic_center(self, a, b, c, d, e, f, g, h, i):
        s = {a, b, c, d, e, f, g, h, i}
        return (len(s) == 9 and min(s) == 1 and max(s) == 9 and
                15 == a + b + c == a + d + g == a + e + i
                   == b + e + h == c + e + g == c + f + i
                   == d + e + f == g + h + i)

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        ret = []
        x, y = 0, 0
        dx, dy = -1, 1
        while x != m - 1 or y != n - 1:
            print x, y
            ret.append(matrix[x][y])
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                if dx == -1 and y != n-1 or dx == 1 and x == m-1:
                    y += 1
                elif dx == -1 and y == n-1 or dx == 1 and x != m-1:
                    x += 1
                dx = -dx
                dy = -dy
            else:
                x += dx
                y += dy
        ret.append(matrix[-1][-1])
        return ret
            
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        ret = [[None for _ in xrange(n)] for _ in xrange(n)]
        corner = {(1,0):0, (0,n-1):1, (n-1,0):3, (n-1, n-1):2}
        dir = 0
        i, j = 0, 0
        count = 0
        dir = 0
        while i < n and j < n and count < n**2:
            count += 1
            ret[i][j] = count
            if (i, j) in corner:
                dir = corner[(i, j)]
                del corner[(i, j)]
                if dir == 0:
                    corner[(i+1, j+1)] = dir
                elif dir == 1:
                    corner[(i+1, j-1)] = dir
                elif dir == 2:
                    corner[(i-1, j-1)] = dir
                elif dir == 3:
                    corner[(i-1, j+1)] = dir
            if dir == 0:
                j += 1
            elif dir == 1:
                i += 1
            elif dir == 2:
                j -= 1
            elif dir == 3:
                i -= 1
        return ret
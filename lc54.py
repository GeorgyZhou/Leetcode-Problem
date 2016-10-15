class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        if m == 1 or n ==1:
            for i in xrange(m):
                for j in xrange(n):
                    ret.append(matrix[i][j])
            return ret
        d = 0
        corner = [(1,0), (0,n-1), (m-1,n-1), (m-1,0)]
        x, y = 0, 0
        while len(ret) < m * n:
            ret.append(matrix[x][y])
            if d == 0:
                y += 1
            elif d == 1:
                x += 1
            elif d == 2:
                y -= 1
            elif d == 3:
                x -= 1
            nd = (d+1)%4
            if (x,y) == corner[nd]:
                d = nd
                if nd == 0:
                    corner[nd] = (corner[nd][0]+1, corner[nd][1]+1)
                elif nd == 1:
                    corner[nd] = (corner[nd][0]+1, corner[nd][1]-1)
                elif nd == 2:
                    corner[nd] = (corner[nd][0]-1, corner[nd][1]-1)
                else:
                    corner[nd] = (corner[nd][0]-1, corner[nd][1]+1)
        return ret
                
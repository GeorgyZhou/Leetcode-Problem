class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        self.matrix, self.target = matrix, target
        return self.rec(0, 0, m-1, n-1)
        
        
    def rec(self, startx, starty, endx, endy):
        if endx < startx or endy < starty or self.target < self.matrix[startx][starty] or self.target > self.matrix[endx][endy]:
            return False
        midx, midy = startx + (endx - startx) / 2, starty + (endy - starty) / 2
        if self.target == self.matrix[midx][midy]:
            return True
        elif self.target > self.matrix[midx][midy]:
            for j in xrange(midy+1, endy+1):
                if self.target == self.matrix[midx][j]:
                    return True
            for i in xrange(midx+1, endx+1):
                if self.target == self.matrix[i][midy]:
                    return True
            return self.rec(midx + 1, midy + 1, endx, endy) or self.rec(startx, midy + 1, midx-1, endy) or self.rec(midx+1, starty, endx, midy-1)
        else:
            for i in xrange(startx, midx):
                if self.target == self.matrix[i][midy]:
                    return True
            for j in xrange(starty, midy):
                if self.target == self.matrix[midx][j]:
                    return True
            return self.rec(startx, starty, midx - 1, midy - 1) or self.rec(startx, midy + 1, midx-1, endy) or self.rec(midx+1, starty, endx, midy-1)
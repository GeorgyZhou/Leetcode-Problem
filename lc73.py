class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if row == 0:
            return None
        col = len(matrix[0])
        if col == 0:
            return None
        firstzero = False
        for i in xrange(row):
            if matrix[i][0] == 0:
                firstzero = True
            for j in xrange(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in xrange(row-1, -1, -1):
            for j in xrange(col-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if firstzero:
                matrix[i][0] = 0
        return None
        
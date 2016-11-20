class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.m, self.n = len(matrix), len(matrix[0])
        self.nums = [[0 for _ in xrange(self.n)] for _ in xrange(self.m)]
        self.tree = [[0 for _ in xrange(self.n+1)] for _ in xrange(self.m+1)]
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.update(i, j, matrix[i][j])
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i, j = row+1, col+1
        while i <= self.m:
            while j <= self.n:
                self.tree[i][j] += delta
                j += (j & (-j))
            i += (i & (-i))
        return

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum(row1, col1) + self.sum(row2, col2) - self.sum(row1, col2) - self.sum(row2, col1)
    
    def sum(self, row, col):
        ret = 0
        i, j = row+1, col+1
        while i > 0:
            while j > 0:
                ret += self.tree[i][j]
                j -= (j & (-j))
            i -= (i & (-i))
        return ret
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return
        r = n / 2
        for i in xrange(r):
            tmp = [matrix[j][i] for j in xrange(n - i - 1, i - 1, -1)]
            for j in xrange(i, n - i, 1):
                s = matrix[i][j]
                matrix[i][j] = tmp[j - i]
                tmp[j-i] = s if j != i else tmp[-1]
            for j in xrange(i, n - i, 1):
                s = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp[j - i]
                tmp[j - i] = s if j != i else tmp[-1]
            for j in xrange(i, n - i, 1):
                s = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = tmp[j - i]
                tmp[j - i] = s if j != i else tmp[-1]
            for j in xrange(i, n - i, 1):
                s = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = tmp[j - i]
                tmp[j - i] = s if j != i else tmp[-1]
        return

s = Solution()
s.rotate([[1,2],[3,4]])
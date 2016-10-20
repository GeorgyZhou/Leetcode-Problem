class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return True
        up, down = 0, row-1
        while up <= down:
            middle = up + (down - up) / 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] > target:
                down = middle-1
            elif matrix[middle][0] < target:
                up = middle+1
        row = middle if matrix[middle][0] < target else middle - 1
        if row < 0:
            return False
        left, right = 0, col-1
        while left <= right:
            middle = left + (right - left) / 2
            print row, middle
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                right = middle-1
            else:
                left = middle+1
        return False
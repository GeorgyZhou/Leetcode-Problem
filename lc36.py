class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        used_row = [[False] * 9 for _ in xrange(9)]
        used_col = [[False] * 9 for _ in xrange(9)]
        used_block = [[False] * 9 for _ in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    print num
                    k = i / 3 * 3 + j / 3
                    if used_row[i][num] or used_block[k][num] or used_col[j][num]:
                        return False
                    used_block[k][num], used_row[i][num], used_col[j][num] = True, True, True
        return True
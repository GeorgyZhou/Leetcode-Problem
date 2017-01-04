class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0
        if not board:
            return ret
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (j == 0 or board[i][j-1] == '.') and (i == 0 or board[i-1][j] == '.'):
                    ret += 1
        return ret
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        index = []
        row, col = len(board), len(board[0])
        if row == 1 or col == 1:
            for i in xrange(row):
                for j in xrange(col):
                    board[i][j] = 0
            return
        for i in xrange(row):
            for j in xrange(col):
                f1, f2, f3, f4 = i-1<0, j-1<0, i+1>=row, j+1>=col
                live = 0
                if f1 and f2:
                    live = board[i+1][j] + board[i+1][j+1] + board[i][j+1]
                elif f1 and f4:
                    live = board[i+1][j-1] + board[i+1][j] + board[i][j-1]
                elif f3 and f2:
                    live = board[i-1][j] + board[i-1][j+1] +board[i][j+1]
                elif f3 and f4:
                    live = board[i-1][j] + board[i][j-1] + board[i-1][j-1]
                elif f1:
                    live = board[i][j-1] + board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j-1]
                elif f2:
                    live = board[i+1][j] + board[i-1][j] + board[i+1][j+1] + board[i-1][j+1] + board[i][j+1]
                elif f3:
                    live = board[i][j-1] + board[i][j+1] + board[i-1][j] + board[i-1][j+1] + board[i-1][j-1]
                elif f4:
                    live = board[i][j-1] + board[i+1][j-1] + board[i-1][j-1] + board[i+1][j] + board[i-1][j]
                else:
                    live = board[i-1][j-1] + board[i-1][j] + board[i-1][j+1] + board[i][j-1] + board[i][j+1]\
                           + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
                print i+1, j+1, live
                if (live > 3 or live < 2) and board[i][j] == 1:
                    index.append((i,j))
                elif live == 3 and board[i][j] == 0:
                    index.append((i,j))
        for tuple in index:
            board[tuple[0]][tuple[1]] = 1 if board[tuple[0]][tuple[1]] == 0 else 0
        return

s = Solution()
print s.gameOfLife([[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,1,1,0,0],[0,0,0,0,0,0]])
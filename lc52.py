class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.count = 0
        self.board = [['.' for _ in xrange(n)] for _ in xrange(n)]
        self.solve(0)
        return self.count
        
    def solve(self, start):
        for i in xrange(self.n):
            if self.isSafe(i, start):
                self.board[i][start] = 'Q'
                if start == self.n-1:
                    self.count += 1
                else:
                    self.solve(start + 1)
                self.board[i][start] = '.'
                     
    def isSafe(self, i, j):
        if self.checkrow(i,j) and self.checkdiag(i,j):
            return True
    
    def checkrow(self, i, j):
        for k in xrange(self.n):
            if k != j and self.board[i][k] == 'Q':
                return False
        return True
    
    def checkdiag(self, i, j):
        x, y = i-1, j-1
        while 0 <= x < self.n and 0 <= y < self.n:
            if self.board[x][y] == 'Q':
                return False
            x -= 1
            y -= 1
        x, y = i+1, j+1
        while 0 <= x < self.n and 0 <= y < self.n:
            if self.board[x][y] == 'Q':
                return False
            x += 1
            y += 1
        x, y = i-1, j+1
        while 0 <= x < self.n and 0 <= y < self.n:
            if self.board[x][y] == 'Q':
                return False
            x -= 1
            y += 1
        x, y = i+1, j-1
        while 0 <= x < self.n and 0 <= y < self.n:
            if self.board[x][y] == 'Q':
                return False
            x += 1
            y -= 1
        return True
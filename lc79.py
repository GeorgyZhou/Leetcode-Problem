class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.n = len(word)
        self.row = len(board)
        self.visited = dict()
        if self.n == 0:
            return True
        if self.row == 0:
            return False
        self.col = len(board[0])
        if self.col == 0:
            return False
        self.board = board
        self.word = word
        for i in xrange(self.row):
            for j in xrange(self.col):
                if self.rec(0, i, j):
                    return True
        return False

    def rec(self, wi, x, y):
        l, u, r, d = False, False, False, False
        if self.board[x][y] == self.word[wi]:
            if wi + 1 == self.n:
                return True
            self.visited[(x,y)] = 1
            if x > 0 and (x-1, y) not in self.visited:
                u = self.rec(wi + 1, x - 1, y)
            if x < self.row - 1 and (x+1, y) not in self.visited:
                d = self.rec(wi + 1, x + 1, y)
            if y < self.col - 1 and (x, y+1) not in self.visited:
                r = self.rec(wi + 1, x, y + 1)
            if y > 0 and (x, y-1) not in self.visited:
                l = self.rec(wi + 1, x, y - 1)
            if not (u or d or r or l):
                del self.visited[(x,y)]
                return False
            else:
                return True
        else:
            return False
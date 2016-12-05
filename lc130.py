class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def findroot(root, x):
            while x is not None and x in root and root[x] != x:
                x = root[x]
            return x
        if not board:
            return
        root = dict()
        m, n = len(board), len(board[0])
        if m < 3 or n < 3:
            return
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        root[(i,j)] = None
                        for x, y in [(i-1, j), (i, j-1)]:
                            if (x, y) in root:
                                r = findroot(root, (x,y))
                                if r is not None:
                                    root[r] = None
                    else:
                        r1 = r2 = (-1, -1)
                        if 0 <= i-1 < m and 0 <= j < n and (i-1,j) in root:
                            r1 = findroot(root, (i-1,j))
                        if 0 <= j-1 < n and 0 <= i < m and (i,j-1) in root:
                            r2 = findroot(root, (i,j-1))
                        if r1 is None or r2 is None:
                            root[r1] = None
                            root[r2] = None
                            root[(i,j)] = None
                        elif r1 == (-1,-1) and r2 == (-1,-1):
                            root[(i,j)] = (i,j)
                        elif r1 == (-1,-1):
                            root[(i,j)] = r2
                        elif r2 == (-1, -1):
                            root[(i,j)] = r1
                        else:
                            root[r1] = r2
                            root[(i,j)] = r2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and findroot(root, (i,j)) is not None:
                    board[i][j] = 'X'
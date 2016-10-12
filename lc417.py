class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        if col == 0:
            return []
        ret = []
        pac = dict()
        alt = dict()
        heapalt = []
        heappac = []
        pacvisited = dict()
        altvisited = dict()
        for i in xrange(row):
            pac[(i,0)] = 1
            pacvisited[(i,0)] = 1
            alt[(i,col-1)] = 1
            altvisited[(i, col-1)] = 1
            heapq.heappush(heapalt, (matrix[i][col-1], i, col-1))
            heapq.heappush(heappac, (matrix[i][0], i, 0))
        for j in xrange(1, col):
            pac[(0,j)] = 1
            pacvisited[(0, j)] = 1
            alt[(row-1, col-1-j)] = 1
            altvisited[(row-1, col-1-j)] = 1
            heapq.heappush(heappac, (matrix[0][j], 0, j))
            heapq.heappush(heapalt, (matrix[row-1][col-1-j], row-1, col-1-j))
        while len(heappac) > 0:
            height, i, j = heapq.heappop(heappac)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < row and 0<= y < col and not pacvisited.has_key((x, y)) and height <= matrix[x][y]:
                    pac[(x,y)] = 1
                    heapq.heappush(heappac, (matrix[x][y], x, y))
                    pacvisited[(x,y)] = 1
        while len(heapalt) > 0:
            height, i, j = heapq.heappop(heapalt)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < row and 0<= y < col and not altvisited.has_key((x, y)) and height <= matrix[x][y]:
                    alt[(x,y)] = 1
                    heapq.heappush(heapalt, (matrix[x][y], x, y))
                    altvisited[(x,y)] = 1
                    
        for x in xrange(row):
            for y in xrange(col):
                if alt.has_key((x, y)) and pac.has_key((x, y)):
                    ret.append([x, y])
        return ret
                    
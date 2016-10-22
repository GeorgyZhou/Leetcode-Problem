class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = []
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while len(queue) > 0:
            x, y = queue[0]
            del queue[0]
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
                    rooms[nx][ny] = rooms[x][y]+1
                    queue.append((nx, ny))
        return
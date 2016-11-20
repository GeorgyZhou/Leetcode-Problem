class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import sys
        if not grid:
            return -1
        min_cost = sys.maxint
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                count += 1 if grid[i][j] == 1 else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res = self.bfs(grid, (i, j, 0), count, min_cost)
                    if res > 0:
                        min_cost = min(res, min_cost)
        return min_cost if min_cost != sys.maxint else -1
        
    def bfs(self, grid, start, buildings, cur_cost):
        from collections import deque
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append(start)
        dis, count = 0, 0
        cost = 0
        visited = {(start[0], start[1])}
        while len(queue) > 0 and count < buildings:
            i, j, dis = queue.popleft()
            if grid[i][j] == 1:
                cost += dis
                if cost >= cur_cost:
                    return cur_cost
                count += 1
            elif grid[i][j] == 0:
                for (x, y) in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] != 2:
                        queue.append((x, y, dis+1))
                        visited.add((x, y))
        return cost if count == buildings else -1
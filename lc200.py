class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        lands = dict()
        islands = dict()
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1':
                    lands[(i, j)] = 1
        count = 0
        while len(lands.keys()) > 0:
            queue = [lands.keys()[0]]
            lands.pop(queue[0], None)
            count += 1
            while len(queue) > 0:
                cur = queue[0]
                del queue[0]
                islands[cur] = count
                if (cur[0]-1, cur[1]) in lands:
                    lands.pop((cur[0]-1, cur[1]), None)
                    queue.append((cur[0]-1, cur[1]))
                if (cur[0]+1, cur[1]) in lands:
                    lands.pop((cur[0]+1, cur[1]), None)
                    queue.append((cur[0]+1, cur[1]))
                if (cur[0], cur[1]+1) in lands:
                    lands.pop((cur[0], cur[1]+1))
                    queue.append((cur[0], cur[1] + 1))
                if (cur[0], cur[1]-1) in lands:
                    lands.pop((cur[0], cur[1]-1))
                    queue.append((cur[0], cur[1] - 1))

        return count

s = Solution()
print s.numIslands(["1111"])
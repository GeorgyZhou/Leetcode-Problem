class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        def findRoot(xy):
            while root[xy] != xy:
                xy = root[xy]
            return xy
        root = dict()
        size = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                cur_root = None
                for x, y in [(i-1, j), (i, j-1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                        new_root = findRoot((x, y))
                        if cur_root is None:
                            cur_root = new_root
                            continue
                        if size[cur_root] <= size[new_root]:
                            root[cur_root] = new_root
                            size[new_root] += size.pop(cur_root)
                            cur_root = new_root
                        else:
                            root[new_root] = cur_root
                            size[cur_root] += size.pop(new_root)
                cur_root = cur_root if cur_root else (i, j)
                root[(i, j)] = cur_root
                size[cur_root] = size.get(cur_root, 0) + 1
        return len(size)
                            
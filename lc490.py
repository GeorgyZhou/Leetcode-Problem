class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        import collections
        visited = set()
        queue = collections.deque()
        queue.append(start)
        while queue:
            x, y = queue.pop()
            visited.add((x, y))
            if x == destination[0] and y == destination[1]:
                return True
            dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for direc in dirs:
                nx, ny = x, y
                while 0 <= nx + direc[0] < len(maze) and 0 <= ny + direc[1] < len(maze[0]) and maze[nx + direc[0]][ny + direc[1]] != 1:
                    nx += direc[0]
                    ny += direc[1]
                if (nx, ny) not in visited:
                    queue.appendleft((nx, ny))
        return False
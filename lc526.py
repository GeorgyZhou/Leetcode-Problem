class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        visited = set()
        self.num = N
        self.count = 0
        self.dfs(1, visited)
        return self.count
        
    def dfs(self, pos, visited):
        if pos > self.num:
            self.count += 1
            return
        for i in range(1, self.num + 1):
            if i not in visited and (i % pos == 0 or pos % i == 0):
                visited.add(i)
                self.dfs(pos+1, visited)
                visited.remove(i)
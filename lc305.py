class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        count = 0
        self.size = dict()
        self.root = dict()
        for i, j in positions:
            root = None
            for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) in self.root:
                    tmp_root = self.find_root(x, y)
                    if root is None:
                        root = tmp_root
                        self.root[(i, j)] = root
                        self.size[root] += 1
                    elif tmp_root != root:
                        if self.size[tmp_root] > self.size[root]:
                            self.size[tmp_root] += self.size[root]
                            self.root[root] = tmp_root
                            del self.size[root]
                            root = tmp_root
                            self.root[(i, j)] = root
                            self.size[root] += 1
                        else:
                            self.size[root] += self.size[tmp_root] + 1
                            self.root[tmp_root] = root
                            del self.size[tmp_root]
                            self.root[(i, j)] = root
                            self.size[root] += 1
                        count -= 1
            if root is None:
                count += 1
                self.root[(i, j)] = (-1, -1)
                self.size[(i, j)] = 1
            ret.append(count)
        return ret
            
    
    def find_root(self, x, y):
        while self.root[(x, y)] != (-1, -1):
            x, y = self.root[(x, y)]
        return (x, y)
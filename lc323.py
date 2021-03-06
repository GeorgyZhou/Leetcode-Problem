class Solution(object):
    def countComponents(self, n, edges):
        self.root = dict()
        self.parent = dict()
        for x, y in edges:
            if x >= n or y >= n:
                continue
            if x in self.parent and y in self.parent:
                rx = self.find_root(x)
                ry = self.find_root(y)
                if rx == ry:
                    continue
                if self.root[rx] > self.root[ry]:
                    self.parent[ry] = rx
                    del self.root[ry]
                else:
                    self.parent[rx] = ry
                    del self.root[rx]
            elif x in self.parent:
                rx = self.find_root(x)
                self.parent[y] = rx
                self.root[rx] += 1
            elif y in self.parent:
                ry  = self.find_root(y)
                self.parent[x] = ry
                self.root[ry] += 1
            else:
                self.parent[x] = x
                self.root[x] = 2
                self.parent[y] = x
        return n - len(self.parent) + len(self.root)

    def find_root(self, c):
        if c in self.root:
            return c
        else:
            return self.find_root(self.parent[c])

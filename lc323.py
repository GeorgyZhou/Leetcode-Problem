class Solution(object):
    def countComponents(self, n, edges):
        closed = dict()
        connected = dict()
        num = 0
        rest = range(n)
        for x,y in edges:
            if connected.has_key(y):
                connected[y].append(x)
            else:
                connected[y] = [x]
            if connected.has_key(x):
                connected[x].append(y)
            else connected.has_key(x):
                connected[x] = [y]
        while len(rest) > 0:
            queue = [rest[0]]
            del rest[0]
            while len(queue) > 0:
                cur = queue[-1]
                del queue[-1]
                closed[cur] = 1
                for i in connected[cur]:
                    if i in closed
                
            



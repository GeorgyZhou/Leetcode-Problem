class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.vals = dict()
        self.adj = dict()
        for i, eq in enumerate(equations):
            self.vals[tuple(eq)] = values[i]
            if eq[0] not in self.adj:
                self.adj[eq[0]] = [eq[1]]
            else:
                self.adj[eq[0]].append(eq[1])
            if values[i] != 0:
                self.vals[(eq[1], eq[0])] = 1.0 / values[i]
                if eq[1] not in self.adj:
                    self.adj[eq[1]] = [eq[0]]
                else:
                    self.adj[eq[1]].append(eq[0])
        ret = []
        for query in queries:
            res = self.find_val(tuple(query), dict())
            ret.append(res if res else -1.0)
        return ret
    
    def find_val(self, query, visited):
        if query in self.vals:
            return self.vals[query]
        visited[query[0]] = 1
        for inter in self.adj.get(query[0], []):
            if inter in visited:
                continue
            visited[inter] = 1
            res = self.find_val((inter, query[1]), visited)
            if res is not None:
                self.adj[query[0]].append(query[1])
                tmp = res * self.vals[(query[0], inter)]
                self.vals[query] = tmp
                return tmp
            else:
                return None
            del visited[inter]
        return None
        
        
    
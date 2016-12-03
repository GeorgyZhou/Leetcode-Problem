class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import heapq
        self.edges = dict()
        self.rest = dict()
        self.n = len(tickets) + 1
        for start, dest in tickets:
            if start in self.edges:
                heapq.heappush(self.edges[start], dest)
            else:
                self.edges[start] = [dest]
            self.rest[(start, dest)] = self.rest.get((start, dest), 0) + 1
        for key in self.edges:
            self.edges[key].sort()
        ret = ["JFK"]
        self.rec("JFK", ret)
        return ret

    def rec(self, start, ret):
        if len(ret) == self.n:
            return True
        candidates = self.edges.get(start, [])
        for candidate in candidates:
            if self.rest[(start, candidate)] == 0:
                continue
            self.rest[(start, candidate)] -= 1
            ret.append(candidate)
            if self.rec(candidate, ret):
                return True
            else:
                self.rest[(start, candidate)] += 1
                ret.pop()
        return False

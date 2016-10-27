class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = dict()
        income = dict()
        start = list()
        for pr in prerequisites:
            edges[pr[0]] = [pr[1]] if not edges.has_key(pr[0]) else edges[pr[0]] + [pr[1]]
            income[pr[1]] = income.get(pr[1], 0) + 1
        for i in range(numCourses):
            start.append(i) if not income.has_key(i) else None
        while len(start) > 0:
            n = start.pop(0)
            l = len(edges.get(n,[]))
            for i in xrange(l):
                m = edges[n].pop(0)
                if i == l - 1:
                    del edges[n]
                income[m] -= 1
                if income.get(m, 0) == 0:
                    start.append(m)
        if len(edges) > 0:
            return False
        return True
        
        
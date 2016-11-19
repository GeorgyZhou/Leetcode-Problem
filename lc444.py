class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        n = len(org)
        income, edges = dict(), dict()
        for seq in seqs:
            if len(seq) == 1:
                income[seq[0]] = income.get(seq[0], 0)
            for i in xrange(1, len(seq)):
                former, later = seq[i-1], seq[i]
                income[former] = income.get(former, 0)
                income[later] = income.get(later, 0) + (1 if later not in edges.get(former, []) else 0)
                if former in edges:
                    edges[former].add(later)
                else:
                    edges[former] = set([later])
        if len(income) != n:
            return False
        frontier = []
        for i in xrange(1,n+1):
            if income[i] == 0:
                frontier.append(i)
        res = []
        while len(frontier) == 1:
            next_frontier = []
            par = frontier.pop()
            res.append(par)
            if par not in edges:
                break
            for child in edges.get(par, []):
                income[child] -= 1
                if income.get(child) == 0:
                    next_frontier.append(child)
            del edges[par]
            frontier = next_frontier
        if len(edges) == 0 and len(res) == len(org):
            flag = True
            for i in xrange(n):
                if res[i] != org[i]:
                    flag = False
            return flag
        else:
            return False
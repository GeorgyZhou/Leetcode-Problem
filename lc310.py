class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
        	return []
        if n == 1:
        	return [0]
        adj, income = {i:[] for i in xrange(n)}, {i:0 for i in xrange(n)}
        for x, y in edges:
        	adj[x].append(y)
        	adj[y].append(x)
        	income[x] += 1
        	income[y] += 1
        queue = []
        unvisited = {i:1 for i in xrange(n)}
        for node in income:
        	if income[node] == 1: queue.append(node)
        while len(unvisited) > 2:
        	next = []
        	for node in queue:
        		unvisited.pop(node)
        		for n in adj[node]:
        			if n in unvisited:
        				income[n] -= 1
        				if income[n] == 1: next.append(n)
        	queue = next

        return queue

s = Solution()
print s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
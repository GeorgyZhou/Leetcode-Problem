class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        import Queue
        qu = Queue.Queue()
        if n == 0 or n == 1:
            return True
        if n > 1 and len(edges) == 0:
            return False
        parent = dict()
        adjunct = dict()
        checked_list = dict()
        for node1, node2 in edges:
            if node1 in adjunct:
                adjunct[node1].append(node2)
            else:
                adjunct[node1] = [node2]
            if node2 in adjunct:
                adjunct[node2].append(node1)
            else:
                adjunct[node2] = [node1]
        start_node = edges[0][0]
        qu.put(start_node)
        parent[start_node] = -1
        while not qu.empty():
            node = qu.get()
            checked_list[node] = 1
            for next_node in adjunct[node]:
                if next_node == parent[node]:
                    continue
                if next_node in checked_list:
                    return False
                qu.put(next_node)
                parent[next_node] = node
        if len(checked_list.keys()) == n:
            return True
        return False

s = Solution()
s.validTree(5, [[0,1],[0,2],[2,3],[2,4]])


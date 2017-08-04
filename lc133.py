# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        import collections
        if node is None:
            return None
        queue = collections.deque()
        queue.appendleft(node)
        traversed = {node.label: UndirectedGraphNode(node.label)}
        while queue:
            cn = queue.pop()
            for n in cn.neighbors:
                if n.label not in traversed:
                    traversed[n.label] = UndirectedGraphNode(n.label)
                    queue.appendleft(n)
                traversed[cn.label].neighbors.append(traversed[n.label])
        return traversed[node.label]
                
            
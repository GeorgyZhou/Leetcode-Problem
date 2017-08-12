# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        import collections
        self.occur = collections.defaultdict(list)
        self.rec(root)
        ret = []
        for nodes in self.occur.values():
            if len(nodes) >= 2:
                ret.append(nodes[0])
        return ret
    
    def rec(self, node):
        if node:
            key = node.val, self.rec(node.left), self.rec(node.right)
            self.occur[key].append(node)
            return key
        return None
        
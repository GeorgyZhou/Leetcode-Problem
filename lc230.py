# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        for val in self.dfs(root):
            if k == 1:
                return val
            else:
                k -= 1

    def dfs(self, root):
        if root is not None:
            for val in self.dfs(root.left):
                yield val
            yield root.val
            for val in self.dfs(root.right):
                yield val

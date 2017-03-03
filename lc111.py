# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        if root is None:
            return 0
        return self.rec(root, 0, sys.maxint)
    
    def rec(self, root, height, res):
        if root.left is None and root.right is None:
            return height+1
        if root.left:
            res = min(self.rec(root.left, height+1, res), res)
        if root.right:
            res = min(self.rec(root.right, height+1, res), res)
        return res
        
        
        
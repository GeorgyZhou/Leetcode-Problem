# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.rec(root.right, root.left)
    
    def rec(self, r, l):
        if r is None and l is None:
            return True
        elif r is not None and l is not None and r.val == l.val:
            return self.rec(l.left, r.right) and self.rec(l.right, r.left)
        else:
            return False
        
        
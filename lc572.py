# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return t is None
        return self.isEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    
    def isEqual(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.isEqual(t1.left, t2.left) and self.isEqual(t1.right, t2.right)     
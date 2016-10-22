# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        up = sys.maxint
        down = -sys.maxint - 1
        if not root:
            return True
        return self.isValid( root, up, down)
    
    
    def isValid(self, root, up, down):
        if not root:
            return True
        if down < root.val < up:
            return self.isValid(root.left, root.val, down) and self.isValid(root.right, up, root.val)
        else:
            return False
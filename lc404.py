# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        if not root:
            return 0
        self.rec(root, False)
        return self.sum
    
    def rec(self, root, left):
        if root.left:
            self.rec(root.left, True)
        if root.right:
            self.rec(root.right, False)
        if root.right is root.left and left:
            self.sum += root.val
        return
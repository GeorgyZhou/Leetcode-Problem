# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        import sys
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxint - 1)
        self.rec(root)
        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp

    def rec(self, node):
        if not node:
            return
        self.rec(node.left)
        if self.first is None and node.val <= self.prev.val:
            self.first = self.prev
        if self.first is not None and node.val <= self.prev.val:
            self.second = node
        self.prev = node
        self.rec(node.right)

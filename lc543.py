# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.longest = 1
        self.dfs(root)
        return self.longest - 1
        
    def dfs(self, node):
        if not node.left and not node.right:
            return 1
        left, right = 1, 1
        if node.left:
            left = self.dfs(node.left) + 1
        if node.right:
            right = self.dfs(node.right) + 1
        self.longest = max(self.longest, left + right - 1)
        return max(left, right)
        
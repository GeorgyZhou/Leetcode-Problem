# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.path = []
        self.ret = []
        return self.rec(root)
        
    def rec(self, root):
        self.path.append(str(root.val))
        if root.left is not None:
            self.rec(root.left)
        if root.right is not None:
            self.rec(root.right)
        if root.right is root.left:
            self.ret.append('->'.join(self.path))
        self.path.pop()
        return self.ret
        
        
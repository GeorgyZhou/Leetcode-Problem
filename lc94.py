# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        if not root:
            return []
        return self.rec(root)
        
    def rec(self, root):
        if root.left:
            self.rec(root.left)
        self.ret.append(root.val)
        if root.right:
            self.rec(root.right)
        return self.ret
            
            
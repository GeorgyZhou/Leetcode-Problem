# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.anc = None
        self.rec(root, p, q)
        return self.anc
        
    def rec(self, root, p, q):
        res = 2 if root is p else (1 if root is q else 0)
        if root.left:
            res += self.rec(root.left, p, q)
        if root.right:
            res += self.rec(root.right, p, q)
        if res == 3 and self.anc is None:
            self.anc = root
        return res
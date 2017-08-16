# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.longest = 1
        self.rec(root)
        return self.longest
        
    def rec(self, root):
        inc, dec = 1, 1
        if not root.left and not root.right:
            return (inc, dec)
        if root.left:
            sub_res = self.rec(root.left)
            if root.left.val == root.val - 1:
                dec = max(dec, 1 + sub_res[1])
            elif root.left.val == root.val + 1:
                inc = max(inc, 1 + sub_res[0])
        if root.right:
            sub_res = self.rec(root.right)
            if root.right.val == root.val - 1:
                dec = max(dec, 1 + sub_res[1])
            elif root.right.val == root.val + 1:
                inc = max(inc, 1 + sub_res[0])
        self.longest = max(self.longest, inc + dec - 1)
        return (inc, dec)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.left is None:
            return root
        right = []
        left = []
        cur = root
        while cur.left:
            left.append(cur)
            right.append(cur.right)
            cur = cur.left
        newroot = cur
        for i in xrange(len(left)-1, -1, -1):
            cur.left = right[i]
            cur.right = left[i]
            cur = cur.right
        return newroot
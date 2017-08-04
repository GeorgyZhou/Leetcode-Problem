# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        ret = []
        cur = []
        self.rec(root, cur, ret)
        return ret
    
    def rec(self, node, cur, ret):
        cur.append(str(node.val))
        if not node.left and not node.right:
            ret.append('->'.join(cur))
        if node.left:
            self.rec(node.left, cur, ret)
        if node.right:
            self.rec(node.right, cur, ret)
        cur.pop()
        return
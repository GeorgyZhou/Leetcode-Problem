# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.sum = sum
        if not root:
            return self.ret
        self.rec(root, [])
        return self.ret
        
    def rec(self, root, path):
        path.append(root.val)
        if root.left:
            self.rec(root.left, path)
        if root.right:
            self.rec(root.right, path)
        if root.left is None and root.right is None and sum(path) == self.sum:
            tmp = [val for val in path]
            self.ret.append(tmp)
        path.pop()
        return
        
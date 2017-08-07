# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.val_set = set()
        self.res = False
        self.dfs(root, k)
        return self.res
    
    def dfs(self, root, k):
        if not root:
            return 
        if k - root.val in self.val_set:
            self.res = True
            return
        self.val_set.add(root.val)
        self.dfs(root.left, k)
        self.dfs(root.right, k)
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
        :rtype: int
        """
        self.target = sum
        self.ret = 0
        if not root:
            return 0
        self.rec(root, [])
        return self.ret
    
    def rec(self, root, path):
        path.append(root.val)
        total_sum = sum(path)
        if total_sum == self.target:
            self.ret += 1
        for i in range(len(path)-1):
            total_sum -= path[i]
            if total_sum == self.target:
                self.ret += 1
        if root.left:
            self.rec(root.left, path)
        if root.right:
            self.rec(root.right, path)
        path.pop()
        return
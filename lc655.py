# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.height = 0
        self.find_height(root, 1)
        width = (1 << self.height) - 1
        self.res = [["" for _ in range(width)] for _ in range(self.height)]
        self.rec(root, 0, 0, width - 1)
        return self.res
        
    def find_height(self, root, y):
        if not root:
            self.height = max(self.height, y-1)
            return
        self.find_height(root.left, y+1)
        self.find_height(root.right, y+1)
    
    def rec(self, node, y, start, end):
        if not node:
            return
        self.res[y][(start + end) / 2] = str(node.val)
        self.rec(node.left, y + 1, start, (start+end) / 2 - 1)
        self.rec(node.right, y + 1, (start+end) / 2 + 1, end)
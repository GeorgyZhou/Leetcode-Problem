# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        left, right = [], []
        bottom = []
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        if root.left:
            self.getLeft(root, left)
        else:
            left = [root.val]
        if root.right:
            self.getRight(root, right)
        else:
            right = [root.val]
        self.getBottom(root, bottom)
        start = 1 if root.left else 0
        end = -1 if root.right else len(bottom)
        ret = left + bottom[start:end] + right[:-1]
        return ret
    
    def getBottom(self, node, bottom):
        if node is None:
            return
        if node.left is None and node.right is None:
            bottom.append(node.val)
        if node.left:
            self.getBottom(node.left, bottom)
        if node.right:
            self.getBottom(node.right, bottom)
    
    def getLeft(self, node, left):
        left.append(node.val)
        if node.left:
            self.getLeft(node.left, left)
        elif node.right:
            self.getLeft(node.right, left)
    
    def getRight(self, node, right):
        if node.right:
            self.getRight(node.right, right)
        elif node.left:
            self.getRight(node.left, right)
        right.append(node.val)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        array = []
        self.toSortedArray(root, array)
        import sys
        diff = sys.maxint
        for i in range(1, len(array)):
            diff = min(diff, abs(array[i] - array[i-1]))
        return diff
    
    def toSortedArray(self, root, array):
        if root.left:
            self.toSortedArray(root.left, array)
        array.append(root.val)
        if root.right:
            self.toSortedArray(root.right, array)
        
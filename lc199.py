# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        front = [root]
        while len(front) > 0:
            next_front = []
            for node in front:
                if node.left:
                    next_front.append(node.left)
                if node.right:
                    next_front.append(node.right)
            ret.append(node.val)
            front = next_front
        return ret
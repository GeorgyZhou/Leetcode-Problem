# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        import sys
        prev = sys.maxint
        val = None
        cur = root
        while cur:
            prev = min(prev, abs(cur.val - target))
            if prev == abs(cur.val - target):
                val = cur.val 
            if cur.val == target:
                return val
            elif cur.val > target:
                if cur.left:
                    cur = cur.left
                else:
                    return val
            else:
                if cur.right:
                    cur = cur.right
                else:
                    return val
        return val
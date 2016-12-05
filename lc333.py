# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 1
        if not root:
            return 0
        self.rec(root)
        return self.ret
    
    def rec(self, root):
        if root.left and root.right:
            left_num, left_min, left_max = self.rec(root.left)
            right_num, right_min, right_max = self.rec(root.right)
            if left_min is not None and right_min is not None and root.val > left_max and root.val < right_min:
                self.ret = max(left_num + 1 + right_num, self.ret)
                return left_num + 1 + right_num, left_min, right_max
            else:
                return 1, None, None
        elif root.left:
            left_num, left_min, left_max = self.rec(root.left)
            if left_min is not None and root.val > left_max:
                self.ret = max(left_num + 1, self.ret)
                return left_num + 1, left_min, root.val
            else:
                return 1, None, None
        elif root.right:
            right_num, right_min, right_max = self.rec(root.right)
            if right_min is not None and root.val < right_min:
                self.ret = max(right_num + 1, self.ret)
                return right_num + 1, root.val, right_max
            else:
                return 1, None, None
        else:
            return 1, root.val, root.val
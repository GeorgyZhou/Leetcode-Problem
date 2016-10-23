# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        queue = [(root, 0)]
        while len(queue):
            cur, level = queue.pop(0)
            if len(ret) <= level:
                ret.append([cur.val])
            else:
                ret[level].append(cur.val)
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))
        for i in xrange(1, len(ret),2):
            ret[i].reverse()
        return ret
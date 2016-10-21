# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = dict()
        ret = []
        queue = [[root, 1]]
        while len(queue) > 0:
            root, level = queue[0]
            del queue[0]
            if root.left:
                queue.append([root.left, level + 1])
            if root.right:
                queue.append([root.right, level + 1])
            if not dic.has_key(level):
                ret.append([root.val])
                dic[level] = 1
            else:
                ret[-1].append(root.val)
        ret.reverse()
        return ret
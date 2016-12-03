# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        dic = dict()
        low, high = 0, 0
        queue = [(root, 0)]
        while len(queue) > 0:
            next_queue = []
            for node, col in queue:
                low = min(col, low)
                high = max(col, high)
                if col not in dic:
                    dic[col] = [node.val]
                else:
                    dic[col].append(node.val)
                if node.left:
                    next_queue.append((node.left, col-1))
                if node.right:
                    next_queue.append((node.right, col+1))
            del queue
            queue = next_queue
        ret = []
        for i in range(low, high+1, 1):
            ret.append(dic[i])
        return ret
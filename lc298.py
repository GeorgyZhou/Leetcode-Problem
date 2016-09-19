class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        return self.recur(root, 1, root.val)

    def recur(self, node, curr_count, prev):
        if node.val - prev == 1:
            curr_count += 1
        else:
            curr_count = 1
        left_max = 1
        right_max = 1
        if node.left:
            left_max = self.recur(node.left, curr_count, node.val)
        if node.right:
            right_max = self.recur(node.right, curr_count, node.val)
        if not node.left and not node.right:
            return curr_count
        return max(curr_count, left_max, right_max)
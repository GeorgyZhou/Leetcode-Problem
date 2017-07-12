class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        if d == 2:
            left_child = root.left
            right_child = root.right
            node1 = TreeNode(v)
            node2 = TreeNode(v)
            node1.left = left_child
            node2.right = right_child
            root.left = node1
            root.right = node2
            return root
        if root.left:
            self.addOneRow(root.left, v, d-1)
        if root.right:
            self.addOneRow(root.right, v, d-1)
        return root
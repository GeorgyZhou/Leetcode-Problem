# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node, last_node = self.find_node(root, key, None)
        if node is None:
            return root
        subsititute = None
        if node.left is not None:
            subsititute, flag = self.find_substitute(node.left, False)
        elif node.right is not None:
            subsititute, flag = self.find_substitute(node.right, True)
        
        if node.left is not subsititute:
            subsititute.left = node.left
        if node.right is not subsititute:
            subsititute.right = node.right
        if last_node is not None:
            if last_node.left is node:
                last_node.left = subsititute
            else:
                last_node.right = subsititute
        else:
            if subsititute is None:
                return None
            return subsititute
        return root
            
            
        
    def find_node(self, root, key, last_node):
        if root is None:
            return None, None
        if root.val == key:
            return root, last_node
        return self.find_node(root.left, key, root) if root.val > key else self.find_node(root.right, key, root)
        
    
    def find_substitute(self, root, flag):
        if (root.left is None and flag) or (root.right is None and not flag):
            return root, True
        node, change_flag = self.find_substitute(root.left, flag) if flag else self.find_substitute(root.right, flag)
        if change_flag:
            if flag:
                root.left = node.right
            else:
                root.right = node.left
        return node, False
        
        
        
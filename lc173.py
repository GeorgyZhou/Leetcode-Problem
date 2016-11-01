# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def rec(node, ret):
            if node.left:
                rec(node.left, ret)
            ret.append(node.val)
            if node.right:
                rec(node.right, ret)
            return ret
        self.ret = []
        self.pointer = 0
        if not root:
            return
        else:
            rec(root, self.ret)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer < len(self.ret):
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        self.pointer += 1
        return self.ret[self.pointer - 1]
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
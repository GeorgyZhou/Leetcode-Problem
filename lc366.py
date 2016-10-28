# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.ret = []
        self.rec(root)
        return self.ret
        
    def rec(self, root):
        if root.left and root.right:
            l = self.rec(root.left)
            r = self.rec(root.right)
            c = max(l, r)
            # print root.val, c, self.ret
            if len(self.ret) == c:
                self.ret.append([root.val])
            else:
                self.ret[c].append(root.val)
            return c + 1
        elif root.left:
            c = self.rec(root.left)
            if len(self.ret) <= c:
                self.ret.append([root.val])
            else:
                self.ret[c].append(root.val)
            return c + 1
        elif root.right:
            c = self.rec(root.right)
            if len(self.ret) == c:
                self.ret.append([root.val])
            else:
                self.ret[c].append(root.val)
            return c + 1
        else:
            if self.ret:
                self.ret[0].append(root.val)
            else:
                self.ret.append([root.val])
            return 1
            
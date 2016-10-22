# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        self.dp = [[[] for _ in xrange(n+2)] for _ in xrange(n+2)]
        return self.generateTree(1, n)
    
    def generateTree(self, s, e):
        if s > e:
            self.dp[s][e] = [None]
            return self.dp[s][e]
        if self.dp[s][e]:
            return self.dp[s][e]
        for j in xrange(s, e+1):
            for leftTree in self.generateTree(s, j-1):
                for rightTree in self.generateTree(j+1, e):
                    cur = TreeNode(j)
                    cur.left = leftTree
                    cur.right = rightTree
                    self.dp[s][e].append(cur)
        return self.dp[s][e]
        
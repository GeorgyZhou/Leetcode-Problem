class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        self.index = 0
        self.vals = preorder.split(',')
        self.n = len(self.vals)
        self.rec()
        return self.index == self.n

    def rec(self):
        val = self.vals[self.index] if self.index < self.n else '#'
        self.index += 1
        if val == "#":
            return
        self.rec()
        self.rec()

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= 0:
            return True
        if sum(range(1, maxChoosableInteger+1)) < desiredTotal:
            return False
        rest = range(maxChoosableInteger, 0, -1)
        self.mem = dict()
        return self.rec(rest, desiredTotal)

    def rec(self, rest, desiredTotal):
        key = str(rest)
        if key in self.mem:
            return self.mem[key]
        if not rest:
            return False
        elif rest[0] >= desiredTotal:
            return True
        for i, num in enumerate(rest):
            res = self.rec(rest[:i] + rest[i+1:], desiredTotal-num)
            if not res:
                self.mem[key] = True
                return True
        self.mem[key] = False
        return False
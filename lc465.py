class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        import sys
        debt = dict()
        for tr in transactions:
            debt[tr[0]] = debt.get(tr[0], 0) - tr[2]
            debt[tr[1]] = debt.get(tr[1], 0) + tr[2]
        self.debts = []
        for v in debt.values():
            if v != 0:
                self.debts.append(v)
        return self.rec(0, 0)
    
    def rec(self, start, count):
        while start < len(self.debts) and self.debts[start] == 0:
            start += 1
        res = sys.maxint
        prev = 0
        for i in range(start+1, len(self.debts)):
            if self.debts[i] != prev and self.debts[start] * self.debts[i] < 0:
                self.debts[i] += self.debts[start]
                res = min(res, self.rec(start+1, count+1))
                self.debts[i] -= self.debts[start]
                prev = self.debts[i]
        return res if res < sys.maxint else count
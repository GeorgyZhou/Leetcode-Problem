class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.ret = 0
        self.skip = dict()
        self.skip[('1', '3')] = self.skip[('3', '1')] = '2'
        self.skip[('1', '7')] = self.skip[('7', '1')] = '4'
        self.skip[('7', '9')] = self.skip[('9', '7')] = '8'
        self.skip[('3', '9')] = self.skip[('9', '3')] = '6'
        self.skip[('1', '9')] = self.skip[('9', '1')] = self.skip[('3', '7')] = self.skip[('7', '3')] = self.skip[('2', '8')] = self.skip[('8', '2')] = self.skip[('4', '6')] = self.skip[('6', '4')] = '5'
        if m == 1:
            self.ret += 9
        if n == 1:
            return self.ret
        self.rec(m, n, [str(i) for i in range(1, 10)])
        return self.ret
        
    def rec(self, m, n, before):
        cur = []
        for comb in before:
            last = comb[-1]
            candidates = [str(i) for i in '123456789' if i not in comb]
            for next in candidates:
                if (last, next) in self.skip:
                    if self.skip[(last, next)] in comb:
                        newcomb = comb + next
                        cur.append(newcomb)
                else:
                    newcomb = comb + next
                    cur.append(newcomb)
        del before
        level = len(cur[0])
        print level
        if m <= level <= n:
            self.ret += len(cur)
            if level == n:
                return
            else:
                self.rec(m, n, cur)
        else:
            self.rec(m, n, cur)
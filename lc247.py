class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.num = n
        return self.rec(n)
    
    def rec(self, n):
        cand1 = ['1','0','8']
        if n == 0 or n == 1:
            return [""] if n == 0 else cand1
        ret = []
        for i in self.rec(n-2):
            ret.append("6" + i + "9")
            ret.append("9" + i + "6")
            ret.append("8" + i + "8")
            ret.append("1" + i + "1")
            if n != self.num:
                ret.append("0" + i + "0")
        return ret
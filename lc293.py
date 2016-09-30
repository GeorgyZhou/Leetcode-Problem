class Solution(object):
    def generatePossibleNextMoves(self, s):
        n = len(s)
        if n < 2:
            return []
        ret = []
        before = (s[0]=='+')
        for i in xrange(1,n):
            if s[i] == '+' and before:
                ret.append(s[0:i-1] + '--' + s[i+1:n])
            elif s[i] == '+':
                before = True
            else:
                before = False
        return ret

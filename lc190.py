class Solution:
    # @param n, an integer
    # @return an integer
    def __init__(self):
        self.dic = dict()
        
    def reverseBits(self, n):
        if self.dic.has_key(n):
            return self.dic[n]
        bits = []
        tmp = n
        for _ in xrange(32):
            bits.append(n&1)
            n >>= 1
        ret = 0
        for i in bits:
            ret <<= 1
            ret += i
        self.dic[tmp] = ret
        self.dic[ret] = tmp
        return ret
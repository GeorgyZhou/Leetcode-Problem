class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        dic = {i:str(i) for i in range(10)}
        dic[10], dic[11], dic[12], dic[13], dic[14], dic[15] = 'a', 'b', 'c', 'd', 'e', 'f'
        tmp = num if num > 0 else -num
        bits = []
        while tmp != 0:
            bits.append(tmp%2)
            tmp /= 2
        if num < 0:
            first = True
            for i in range(len(bits)):
                if not first:
                    bits[i] = 1-bits[i]
                elif bits[i] == 1 and first:
                    first = False
        while num < 0 and len(bits) < 32:
            bits.append(1)
        bits.reverse()
        
        ret = []
        for index in range(len(bits)-1, -1, -4):
            num = 0
            for i in range(max(0, index-3), index+1, 1):
                num = num * 2 + bits[i]
            ret.append(dic[num])
        ret.reverse()
        return ''.join(ret)
                
                
        
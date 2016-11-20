class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s += "]"
        res, index = self.rec(s, 0)
        return res
    
    def rec(self, s, index):
        i, l = index, len(s)
        ret = ""
        num = 0
        while i < l:
            if s[i] == "[":
                tmp, ni = self.rec(s, i+1)
                ret += (num * tmp)
                num = 0
                i = ni
            elif s[i] == "]":
                return ret, i+1 
            elif "0" <= s[i] <= "9":
                num = num * 10 + int(s[i])
                i += 1
            else:
                ret += s[i]
                i += 1
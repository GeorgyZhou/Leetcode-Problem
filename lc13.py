class Solution(object):
    def romanToInt(self, s):
        I = ["I","II","III","IV" ,"V" ,"VI","VII","VIII","IX"]
        M = ["M", "MM", "MMM"]
        C = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

        ret = 0
        while(len(s) != 0):
            if s[0] == "M":
                for i in range(len(M)-1 , -1, -1):
                    length = len(M[i])
                    if len(s) >= length and M[i] == s[0:length]:
                        s = s[length:len(s)]
                        ret = ret + 1000 * (i+1)
            if len(s) == 0:
                 continue
            if s[0] == "C" or s[0] == "D":
                for i in range(len(C) - 1, -1, -1):
                    length = len(C[i])
                    if len(s) >= length and C[i] == s[0:length]:
                        s = s[length:len(s)]
                        ret = ret + 100 * (i + 1)
            if len(s) == 0:
                continue
            if s[0] == "X" or s[0] == "L":
                for i in range(len(X) - 1, -1, -1):
                    length = len(X[i])
                    if len(s) >= length and X[i] == s[0:length]:
                        s = s[length:len(s)]
                        ret = ret + 10 * (i + 1)
            if len(s) == 0:
                continue
            if s[0] == "I" or s[0] == "V":
                for i in range(len(I) - 1, -1, -1):
                    length = len(I[i])
                    if len(s) >= length and I[i] == s[0:length]:
                        s = s[length:len(s)]
                        ret = ret + i + 1
        return ret

s = Solution()
print s.romanToInt("MDLXX")
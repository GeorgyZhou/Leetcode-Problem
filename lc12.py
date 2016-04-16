class Solution(object):
    def intToRoman(self, num):
        I = ["", "I","II","III","IV" ,"V" ,"VI","VII","VIII","IX","X"]
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

        unit = num % 10
        num = num / 10
        ret = [I[unit]]
        if num != 0:
            unit = num % 10
            num = num / 10
            ret.append(X[unit])
            if num != 0:
                unit = num % 10
                num = num / 10
                ret.append(C[unit])
                if num != 0:
                    unit = num % 10
                    num = num / 10
                    ret.append(M[unit])
        str = ""
        for i in range(len(ret)-1, -1, -1):
            str += ret[i]
        return str
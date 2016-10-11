class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lstrip(' ').rstrip(' ')
        n = len(s)
        if n == 0:
            return False
        dot = False
        negative = False
        positive = False
        e = False
        fenumber = False
        epositive = False
        enegative = False
        enumber = False
        dotnumber = False
        eindex = None
        for index, i in enumerate(s):
            if index == 0 and i == '-' and not negative:
                negative = True
            elif index == 0 and i == '+' and not positive:
                positive = True
            elif e and index == eindex + 1 and i == '+' and not enegative:
                enegative = True
            elif e and index == eindex + 1 and i == '-' and not epositive:
                epositive = True
            elif '0' <= i <= '9':
                if not dotnumber:
                    dotnumber = True
                if not e:
                    fenumber = True
                if e:
                    enumber = True
            elif i == '.' and not dot and not e:
                dot = True
            elif i == 'e' and not e:
                eindex = index
                e = True
            else:
                return False
        return True if ((enumber and fenumber and e) or not e) and ((dot and dotnumber) or not dot) else False
            

s = Solution()
s.isNumber(' 0.1 ')

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = len(num1), len(num2)
        muls = []
        p1 = l1 - 1
        maxl = 0
        while p1 >= 0:
            tmp = []
            for i in xrange(l1-1-p1):
                tmp.append('0')
            carry = 0
            n1 = int(num1[p1])
            p2 = l2 - 1
            while p2 >= 0:
                n2 = int(num2[p2])
                tmp.append(str((n1*n2 + carry) % 10))
                carry = (n1 * n2 + carry) / 10
                p2 -= 1
            p1 -= 1
            while carry != 0:
                tmp.append(str(carry % 10))
                carry /= 10
            tmp.reverse()
            maxl = max(maxl, len(tmp))
            muls.append(''.join(tmp))
        ret = []
        carry = 0
        for i in xrange(-1, -maxl-1, -1):
            s = 0
            for res in muls:
                if abs(i) <= len(res):
                    s += int(res[i])
            ret.append(str((s + carry) % 10))
            carry = (s + carry) / 10
        while carry != 0:
            ret.append(str(carry % 10))
            carry /= 10
        ret.reverse()
        return ''.join(ret)
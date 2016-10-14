class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        if l1 == 0 and l2 == 0:
            return ''
        p1, p2 = l1-1, l2-1
        ret = []
        carry = 0
        while p1 >= 0 and p2 >= 0:
            n1, n2 = int(num1[p1]), int(num2[p2])
            ret.append(str((n1 + n2 + carry) % 10))
            carry = (n1 + n2 + carry) / 10
            p1 -= 1
            p2 -= 1
        while p1 >= 0:
            n1 = int(num1[p1])
            p1 -= 1
            ret.append(str((n1 + carry) % 10))
            carry = (n1 + carry) / 10
        while p2 >= 0:
            n2 = int(num2[p2])
            p2 -= 1
            ret.append(str((n2 + carry) % 10))
            carry = (n2 + carry) / 10
        if carry != 0:
            ret.append(str(carry))
        ret.reverse()
        return ''.join(ret)
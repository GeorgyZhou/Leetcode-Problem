class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a), len(b)
        ret = []
        if lb == 0 and la == 0:
            return ''
        if lb == 0:
            return a
        if la == 0:
            return b
        la -= 1
        lb -= 1
        carry = 0
        while la >= 0 and lb >= 0:
            if carry:
                if a[la] == '1' and b[lb] == '1':
                    ret.append('1')
                elif a[la] == '1' or b[lb] == '1':
                    ret.append('0')
                else:
                    ret.append('1')
                    carry = 0
            else:
                if a[la] == '1' and b[lb] == '1':
                    ret.append('0')
                    carry = 1
                elif a[la] == '1' or b[lb] == '1':
                    ret.append('1')
                else:
                    ret.append('0')
            la -= 1
            lb -= 1
        while la >= 0:
            if carry and a[la] == '1':
                ret.append('0')
            elif carry:
                ret.append('1')
                carry = 0
            else:
                ret.append(a[la])
            la -= 1
        while lb >= 0:
            if carry and b[lb] == '1':
                ret.append('0')
            elif carry:
                ret.append('1')
                carry = 0
            else:
                ret.append(b[lb])
            lb -= 1
        if carry:
            ret.append('1')
        ret.reverse()
        return ''.join(ret)
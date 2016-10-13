class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ret = []
        dic = dict()
        if numerator == 0:
            return '0'
        if numerator * denominator < 0:
            ret.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        bit = numerator / denominator
        sub = numerator % denominator
        ret.append(str(bit))
        if sub == 0:
            return ''.join(ret)
        ret.append('.')
        flag = True
        count = 4 if ret[0] == '-' else 3
        index = -1
        while sub > 0:
            cur = sub * 10
            if dic.has_key(cur):
                index = dic[cur]
                break
            dic[cur] = count - 1
            bit = cur / denominator
            sub = cur % denominator
            count += 1
            ret.append(str(bit))
        if index != -1:
            first = ''.join(ret[0:index])
            second = ''.join(ret[index:count])
            return first + '(' + second + ')'
        return ''.join(ret)

s = Solution()
s.fractionToDecimal(-1,-2147483648)

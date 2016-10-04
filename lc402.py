class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        if k >= n:
            return '0'
        if k == 0:
            return num
        ret = []
        i = 0
        while i < n - 1:
            if num[i] > num[i+1] and k > 0:
                k -= 1
                while len(ret) > 0 and ret[-1] > num[i+1] and k > 0:
                    del ret[-1]
                    k -= 1
                i += 1
            else:
                ret.append(num[i])
                i += 1
        ret.append(num[-1])
        while k > 0:
            del ret[-1]
            k -= 1
        while len(ret) > 0 and ret[0] == '0':
            del ret[0]
        return ''.join(ret) if len(ret) != 0 else '0'

s = Solution()
print s.removeKdigits('1432219', 3)

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        if a/b == -1 and a % b == 0:
            return 0
        sum = (a^b)
        carry = (a&b) << 1
        return Solution.getSum(self, sum, carry)

s = Solution()
print s.getSum(-12, -8)
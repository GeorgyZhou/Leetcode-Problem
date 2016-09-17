class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in xrange(len(digits)-1, -1, -1):
            tmp = carry + digits[i]
            carry = tmp / 10
            digits[i] = tmp % 10
            if carry == 0:
                break
        return [1] + digits if carry == 1 else digits

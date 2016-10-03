class Solution(object):
    def findNthDigit(self, n):
        if n <= 9:
            return n
        i = 0
        num = n
        while num > 0:
            i += 1
            num -= i*9*(10**(i-1))
        num += i*9*(10**(i-1))
        res = str(10**(i-1) + (num-1)/i)
        res = res[num%i-1]
        return int(res)

s = Solution()
print s.findNthDigit(30)

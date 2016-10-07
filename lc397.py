class Solution(object):
    def integerReplacement(self, n):
        step = 0
        while n != 1:
            if n == 3:
                step += 1 
                n = 1
            elif n % 4 == 1:
                n = n - 1
            elif n % 4 == 3:
                n = n + 1
            else:
                n /= 2
            step += 1
        return step

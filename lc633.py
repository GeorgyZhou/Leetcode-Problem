class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        def is_square(num):
            root = math.sqrt(num)
            return int(root) == root
        for i in range(int(math.sqrt(c)) + 1):
            if is_square(c - i**2):
                return True
        return False
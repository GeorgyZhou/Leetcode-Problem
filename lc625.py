class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1:
            return 1
        start = 9
        res = []
        for i in range(start, 1, -1):
            while a != 1 and a % i == 0:
                res.append(i)
                a /= i
            if a == 1:
                break
        
        final_res = 0
        if a == 1:
            for i in range(len(res)):
                final_res += res[i] * (10**i)
        return 0 if final_res > 0x7FFFFFFF else final_res
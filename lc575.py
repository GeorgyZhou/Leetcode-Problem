class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = dict()
        n = len(candies) / 2
        for candy in candies:
            dic[candy] = 1
            if len(dic) > n:
                return n
        return len(dic)
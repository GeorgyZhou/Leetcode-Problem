class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, mask = 0, 0
        for i in range(31, -1, -1):
            prefix_set = set()
            mask = mask | 1 << i
            for num in nums:
                prefix_set.add(num & mask)
            tmp = ret | (1 << i)
            for prefix in prefix_set:
                if tmp ^ prefix in prefix_set:
                    ret = tmp
        return ret
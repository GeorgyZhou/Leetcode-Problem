class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        map = dict()
        for i in nums:
            map[i] = map.get(i, 0) + 1
        for i in map:
            if map[i] == 1:
                ret.append(i)
        return ret
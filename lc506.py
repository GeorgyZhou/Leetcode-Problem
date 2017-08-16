class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sn = sorted(nums, reverse=True)
        dic = dict()
        maps = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        n = len(nums)
        ret = []
        for i in range(n):
            dic[sn[i]] = i + 1
        for i in range(n):
            rank = dic[nums[i]]
            ret.append(maps.get(rank, str(rank)))
        return ret
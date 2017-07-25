class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        sums = 0
        s = dict()
        count = 0
        s[0] = 1
        for num in nums:
            sums += num
            if sums-k in s:
                count += s[sums-k]
            s[sums] = s.get(sums, 0) + 1
        return count
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = dict()
        ret, sum = 0, 0
        for i, num in enumerate(nums):
            sum += num
            if sum == k:
                ret = i + 1
            elif sum - k in sums:
                ret = max(ret, i - sums[sum-k])
            if sum not in sums:
                sums[sum] = i
        return ret
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        ret = n + 1
        left = right = 0
        summary = 0
        while right < n:
            summary += nums[right]
            right += 1
            while summary >= s:
                ret = min(right - left, ret)
                summary -= nums[left]
                left += 1
        return ret if ret <= n else 0
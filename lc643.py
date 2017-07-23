class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_average = sum(nums[:k]) / k
        last_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            last_sum += (nums[i] - nums[i-k])
            max_average = max(last_sum / k, max_average)
        return max_average
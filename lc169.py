class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        n = len(nums)
        if n <= 2:
            return nums[0]
        for num in nums:
            dic[num] = 1 if num not in dic else dic[num] + 1
            if dic[num] > n / 2:
                return num
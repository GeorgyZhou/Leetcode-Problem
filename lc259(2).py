class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in range(len(nums)):
            left, right, t = i + 1, len(nums) - 1, target - nums[i]
            while left < right:
                if nums[left] + nums[right] >= t:
                    right -= 1
                else:
                    count += (right - left)
                    left += 1
        return count
            
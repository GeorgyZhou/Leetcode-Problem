class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        right = length - 1
        left = 0
        while left <= right:
            mid = (right + left) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        pivot = right
        left, right = 0, length - 1
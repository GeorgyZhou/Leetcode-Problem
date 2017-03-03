class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur, last = 0, 0
        while cur < len(nums):
            if nums[cur] != 0:
                tmp = nums[cur]
                nums[cur] = nums[last]
                nums[last] = tmp
                last += 1
            cur += 1
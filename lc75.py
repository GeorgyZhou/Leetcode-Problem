class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cr = cw = cb = 0
        for num in nums:
            if num == 0:
                cr += 1
            elif num == 1:
                cw += 1
            elif num == 2:
                cb += 1
        for i in xrange(len(nums)):
            if i < cr:
                nums[i] = 0
            elif i < cw + cr:
                nums[i] = 1
            else:
                nums[i] = 2
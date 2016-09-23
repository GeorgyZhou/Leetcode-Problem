class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)):
            if i % 2 == 1:
                if nums[i] < nums[i-1]:
                    tmp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = tmp
            elif i != 0 and nums[i-1] < nums[i]:
                tmp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = tmp
        return nums

s = Solution()
print s.wiggleSort([1,2,3,4,5,6])
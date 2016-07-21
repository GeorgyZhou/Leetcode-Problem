class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = 0

        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1

        return res

solution = Solution()
print solution.removeElement([1,2,3,4,5,5,6,6,7,8], 6)
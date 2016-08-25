class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        i = 0
        while i < n:
            if nums[i] != i + 1 and 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
            else:
                i += 1

        for i in xrange(n):
            if nums[i] != i+1:
                return i + 1
        return n + 1

solution = Solution()
print solution.firstMissingPositive([3,4,-1,1])
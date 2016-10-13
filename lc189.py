class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(0, n-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, n-1, nums)
    
    def reverse(self, start, end, nums):
        left, right = start, end
        while left < right:
            nums[left] = nums[left] ^ nums[right]
            nums[right] = nums[left] ^ nums[right]
            nums[left] = nums[left] ^ nums[right]
            left += 1
            right -= 1
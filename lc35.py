class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) / 2
            print left, right, mid
            if nums[mid] < target and (mid == n-1 or (mid != n-1 and nums[mid+1] >= target)):
                return mid + 1
            elif nums[mid] > target and (mid == 0 or (mid != 0 and nums[mid-1] < target)):
                return mid
            elif nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

solution = Solution()
print solution.searchInsert([1, 3], 4)
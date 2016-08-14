class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

solution = Solution()
print solution.search([5,6,7,8,9,0,1,2,3,4], 5)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)-1
        while right >= left:
            mid = left + (right - left) / 2
            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == len(nums) - 1 and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid+1] < nums[mid] > nums[mid-1]:
                return mid
            elif nums[right] >= nums[mid+1] and nums[mid+1] > nums[mid]:
                left = mid + 1
            elif nums[left] >= nums[mid-1] and nums[mid-1] > nums[mid]:
                right = mid - 1
            elif nums[left] <= nums[mid-1] < nums[mid]  < nums[mid+1] and nums[mid+1] >= nums[right]:
                left = mid + 1
            elif nums[right] <= nums[mid+1] < nums[mid] < nums[mid-1] and nums[mid-1] >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1

s = Solution()
print s.findPeakElement([3,2,1])


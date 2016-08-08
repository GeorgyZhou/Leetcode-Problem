class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                left = i + 1
        if left == 0:
            nums.reverse()
        else:
            pivot = left
            for j in xrange(left, len(nums), 1):
                if nums[pivot] >= nums[j] and nums[j] > nums[left - 1]:
                    pivot = j
            tmp = nums[pivot]
            nums[pivot] = nums[left - 1]
            nums[left - 1] = tmp
            for k in xrange(left, (len(nums) + left) / 2, 1):
                right = len(nums) - 1 + left - k
                print k, right
                tmp = nums[k]
                nums[k] = nums[right]
                nums[right] = tmp
        #return
        print nums

solution = Solution()
solution.nextPermutation([5,4,7,5,3,2])

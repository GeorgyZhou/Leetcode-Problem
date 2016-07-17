class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 4:
            return res
        nums.sort()
        if nums[0] * 4 > target or nums[len(nums)-1] * 4 < target:
            return res

        for i in xrange(len(nums) - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in xrange(i + 1, len(nums) - 2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                l, r = j + 1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l+1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res
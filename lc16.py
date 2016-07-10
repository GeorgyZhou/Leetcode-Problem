class Solution(object):
    def threeSum(self, nums, target):
        nums.sort()
        clos
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1
                else:
                    res = [nums[i], nums[l], nums[r]]
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
        return res

solution = Solution()
print
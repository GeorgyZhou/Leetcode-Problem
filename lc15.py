class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
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
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
        return res


solution = Solution()
print 'result:'
print solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
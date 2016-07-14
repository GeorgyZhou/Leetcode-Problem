class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = 0x7FFFFFFF
        for i in xrange(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                if abs(s - target) < diff:
                    s1 = s
                    diff = abs(s - target)
                if s > target:
                    r -= 1
                else:
                    l += 1
        return s1

solution = Solution()
print solution.threeSumClosest([0,2,1,-3], 1)
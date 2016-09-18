class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ret = []
        if not nums:
            return [str(lower) + '->' + str(upper)] if lower != upper else [str(lower)]
        if nums[0] == lower + 1:
            ret.append(str(lower))
        elif nums[0] != lower and nums[0] != lower + 1:
            ret.append(str(lower)+'->'+str(nums[0]-1))
        for i in xrange(len(nums)-1):
            if nums[i]+2 == nums[i+1]:
                ret.append(str(nums[i]+1))
            elif nums[i]+1 == nums[i+1]:
                continue
            else:
                ret.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        if nums[-1] == upper-1:
            ret.append(str(upper))
        elif nums[-1] != upper and nums[-1] != upper-1:
            ret.append(str(nums[-1]+1)+'->'+str(upper))
        return ret

s = Solution()
print s.findMissingRanges([0,1], 0, 2)

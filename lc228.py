class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ret = []
        count = []
        for i in xrange(len(nums)):
            if len(count) == 0 or nums[i] == nums[i-1] + 1:
                count.append(nums[i])
            else:
                if len(count) == 1:
                    ret.append(str(count[0]))
                else:
                    ret.append(str(count[0])+'->'+str(count[-1]))
                count[:] = []
                count.append(nums[i])
        if len(count) == 1:
            ret.append(str(count[0]))
        else:
            ret.append(str(count[0]) + '->' + str(count[-1]))
        return ret

s = Solution()
print s.summaryRanges([0,0,1,1,1])
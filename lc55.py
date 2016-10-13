class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0 or n == 1:
            return True
        start = 0
        end = start + nums[start]
        while start < end:
            if end >= n-1:
                return True
            maxnum, index = nums[start+1]+start+1, start+1
            for i in xrange(start+1, end+1):
                if nums[i] + i > maxnum:
                    maxnum = nums[i] + i
                    index = i
            start = end
            end = maxnum
        if end >= n-1:
            return True
        else:
            return False
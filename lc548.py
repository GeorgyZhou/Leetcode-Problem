class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i-1] + nums[i])
        for j in xrange(3, len(nums) - 3):
            s = dict()
            for i in xrange(1, j-1):
                if sums[j-1] - sums[i] == sums[i-1]:
                    s[sums[i-1]] = 1
            for k in xrange(j+2, len(nums)-1):
                if sums[len(nums)-1] - sums[k] == sums[k-1] - sums[j]:
                    if sums[k-1] - sums[j] in s:
                        return True
        return False
            
            
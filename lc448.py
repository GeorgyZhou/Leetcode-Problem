class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, n = 0, len(nums)
        while i < n:
            while nums[i] != nums[nums[i] - 1]:    
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
            i += 1
        ret = []
        for i in xrange(n):
            if nums[i] != i + 1:
                ret.append(i+1)
        return ret
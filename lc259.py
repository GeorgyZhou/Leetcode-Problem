class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return 0
        nums.sort()
        count = 0
        for i in xrange(n-2):
            j, k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] + nums[i] < target:
                    count += (k - j)
                    j += 1
                else:
                    k -= 1
        return count
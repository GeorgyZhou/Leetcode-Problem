class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)

        res = [0 for _ in xrange(target + 1)]
        for i in xrange(1, target + 1, 1):
            for j in xrange(n):
                if nums[j] == i:
                    res[i] += 1
                elif nums[j] < i:
                    res[i] += res[i - nums[j]]
        return res[target]

solution = Solution()
print solution.combinationSum4([3,2,1], 4)
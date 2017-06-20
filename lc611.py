class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        n = len(nums)
        ret = 0
        for i in range(n-2):
            last = i + 2
            for j in range(i+1, n-1, 1):
                while last < n and nums[i] + nums[j] > nums[last]:
                    last += 1
                ret += (last - j - 1) if last > j else 0
        return ret
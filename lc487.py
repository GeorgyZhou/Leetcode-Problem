class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        forward = [1 if nums[0] else 0]
        for i in range(1, n):
            if nums[i]:
                forward.append(forward[-1] + 1)
            else:
                forward.append(0)
        ret = max(forward)
        prev = 0
        maximum = -1
        for i in range(n-1, -1, -1):
            if forward[i] and prev == 0:
                maximum = forward[i]
            if forward[i] == 1 and prev:
                forward[i] = maximum
            prev = forward[i]
        for i in range(n):
            if nums[i] == 0:
                fellow = forward[i-1] if i else 0
                follow = forward[i+1] if i < n-1 else 0
                ret = max(ret, fellow + 1 + follow)
        return ret
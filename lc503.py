class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        res = [-1 for _ in range(n)]
        for _ in range(2):
            for i in range(n-1, -1, -1):
                while len(stack) != 0 and stack[-1] <= nums[i]:
                    stack.pop()
                stack.append(nums[i])
                res[i] = -1 if len(stack) == 1 else stack[-2]
        return res
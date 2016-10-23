class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        dq = deque()
        n = len(nums)
        ret = []
        for i in xrange(n):
            if len(dq) > 0 and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ret.append(nums[dq[0]])
        return ret
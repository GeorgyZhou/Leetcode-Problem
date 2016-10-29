class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            import sys
            return -sys.maxint - 1
        import heapq
        window = []
        nums = list(set(nums))
        heapq.heapify(window)
        for n in nums:
            if len(window) < 3:
                heapq.heappush(window, n)
            elif window[0] < n:
                heapq.heappushpop(window, n)
        return window[0] if len(window) == 3 else max(window)
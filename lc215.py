class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        n = len(nums)
        heapq.heapify(nums)
        for i in xrange(n - k):
            heapq.heappop(nums)
        return nums[0]
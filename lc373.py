class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        ret = []
        n1, n2 = len(nums1), len(nums2)
        if k >= n1 * n2:
            return [[i, j] for i in nums1 for j in nums2]
        heap = [(i + nums2[0], i, 0) for i in nums1]
        heapq.heapify(heap)
        for i in xrange(k):
            p_sum, num1, index = heap[0][0], heap[0][1], heap[0][2]
            ret.append([num1, p_sum - num1])
            if index + 1 == n2:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (nums2[index+1] + num1, num1, index + 1))
        return ret

solution = Solution()
print solution.kSmallestPairs([1,1,2], [1,2,3], 10)
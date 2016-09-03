class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        h = [(row[0], row, 1) for row in matrix]
        heapq.heapify(h)

        for i in xrange(k-1):
            val, row, index = h[0]
            if index < len(row):
                heapq.heapreplace(h, (row[index], row, index + 1))
            else:
                heapq.heappop(h)
        return h[0][0]
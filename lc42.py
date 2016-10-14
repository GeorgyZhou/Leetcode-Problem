class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        import heapq
        heap = []
        visited = 2
        heapq.heappush(heap, (height[0], 0, 0))
        heapq.heappush(heap, (height[n - 1], 1, n - 1))
        count = 0
        while visited < n:
            h, r, i = heapq.heappop(heap)
            index = i - 1 if r == 1 else i + 1
            visited += 1
            count += max(0, h - height[index])
            heapq.heappush(heap, (max(h, height[index]), r, index))
        return count


s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
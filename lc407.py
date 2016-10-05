class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        row = len(heightMap)
        if row <= 2:
            return 0
        col = len(heightMap[0])
        if col <= 2:
            return 0
        heap = []
        closed = [[0]*col for _ in xrange(row)]
        for i in xrange(row):
            closed[i][0] = 1
            closed[i][col-1] = 1
            heapq.heappush(heap, (heightMap[i][col-1], i, col-1))
            heapq.heappush(heap, (heightMap[i][0], i, 0))
        for i in xrange(col):
            closed[0][i] = 1
            closed[row-1][i] = 1
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            heapq.heappush(heap, (heightMap[row-1][i], row-1, i))
        vol = 0
        while len(heap) > 0:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if 0 <= x < row and 0 <= y < col and closed[x][y] == 0:
                    vol += max(0, height - heightMap[x][y])
                    closed[x][y] = 1
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
        return vol

s = Solution()
s.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])

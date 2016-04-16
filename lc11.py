class Solution(object):
    def maxArea(self, height):
        water = 0
        i, j = 0, len(height) - 1
        while i < j:
            h = height[i] if height[i] < height[j] else height[j]
            water = h * (j - i) if h * (j - i) > water else water
            while( height[i] <= h and i < j ):
                i = i + 1
            while( height[j] <= h and i < j):
                j = j - 1
        return water

s = Solution()
print s.maxArea([1,1])
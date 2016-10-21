class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        ret = 0
        for i in xrange(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                h = heights[stack[-1]]
                stack.pop()
                ret = max(ret, h * (i if not stack else i - 1 - stack[-1]))
            stack.append(i)
        return ret
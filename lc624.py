class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        low, high = None, None
        low_index, high_index = None, None
        s_low, s_high = None, None
        s_low_index, s_high_index = None, None
        for i, array in enumerate(arrays):
            if low is None or array[0] <= low:
                s_low = low
                s_low_index = low_index
                low_index = i
                low = array[0]
            elif s_low is None or array[0] <= s_low:
                s_low = array[0]
                s_low_index = i
            if high is None or array[-1] >= high:
                s_high = high
                s_high_index = high_index
                high_index = i
                high = array[-1]
            elif s_high is None or array[-1] >= s_high:
                s_high = array[-1]
                s_high_index = i
        print(s_low_index, s_high_index, low, high, s_low, s_high)
        if high_index == low_index:
            return max(high - s_low, s_high - low)
        else:
            return high - low
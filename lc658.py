class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import collections
        low, high = 0, len(arr) - 1
        while low < high:
            medium = low + (high - low) / 2
            if arr[medium] > x:
                high = medium
            elif arr[medium] < x:
                low = medium + 1
            else:
                high = medium
                break
        if high < 0:
            return arr[:k]
        if high == len(arr) - 1:
            return arr[-k:]
        left, right = 0, 0
        res = collections.deque()
        low = high - 1
        while len(res) < k:
            if high >= len(arr):
                res.appendleft(arr[low])
                low -= 1
                continue
            if low < 0:
                res.append(arr[high])
                high += 1
                continue
            if abs(arr[high] - x) < abs(arr[low] - x):
                res.append(arr[high])
                high += 1
            else:
                res.appendleft(arr[low])
                low -= 1
        return list(res)
            
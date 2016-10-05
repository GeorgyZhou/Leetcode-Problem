# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        n = len(intervals)
        if n <= 1:
            return n
        heap = []
        for i in xrange(n):
            heapq.heappush(heap, (intervals[i].start, 1, i))
            heapq.heappush(heap, (intervals[i].end, 0, i))
        ret = 0
        proc = dict()
        while len(heap) > 0:
            time, start, index = heapq.heappop(heap)
            if start:
                proc[index] = 1
            else:
                del proc[index]
            ret = max(len(proc), ret)
        return ret

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        n = len(intervals)
        if n <= 1:
            return True
        proc = -1
        heap = []
        import heapq
        for i in xrange(n):
            heapq.heappush(heap, (intervals[i].start, 1, i))
            heapq.heappush(heap, (intervals[i].end, 0, i))
        while len(heap) > 0:
            time, start, index = heapq.heappop(heap)
            if not start and index == proc:
                proc = -1
            elif start and proc == -1:
                proc = index
            else:
                return False
        return True
        
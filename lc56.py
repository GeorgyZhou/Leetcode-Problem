# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        n = len(intervals)
        if n <= 1:
            return intervals
        import heapq
        heap = []
        dic = dict()
        lst = None
        for i in xrange(n):
            heapq.heappush(heap, (intervals[i].start, 0, i))
            heapq.heappush(heap, (intervals[i].end, 1, i))
        while len(heap) > 0:
            time, start, index = heapq.heappop(heap)
            if start == 0:
                if len(dic) == 1 and lst is None:
                    lst = intervals[dic.keys()[0]].start
                dic[index] = 1
            else:
                if len(dic) == 1 and index in dic and lst is None:
                    ret.append(intervals[index])
                elif len(dic) == 1 and index in dic and lst is not None:
                    ret.append(Interval(lst, intervals[index].end))
                    lst = None
                del dic[index]
        return ret
                    
                
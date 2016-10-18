# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        start, end = newInterval.start, newInterval.end
        inserted = False
        res = []
        for i in xrange(len(intervals)):
            if inserted or intervals[i].end < start:
                res.append(intervals[i])
            elif intervals[i].start > end:
                res.append(Interval(start, end))
                res.append(intervals[i])
                inserted = True
            else:
                if intervals[i].start < start:
                    start = intervals[i].start
                if intervals[i].end > end:
                    end = intervals[i].end
        if not inserted:
            res.append(Interval(start, end))
        
        return res
                
            
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
        for i in xrange(len(intervals)-1):
            for j in xrange(i+1, len(intervals)):
                if intervals[i].start >= intervals[j].end or intervals
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.dq = deque()
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.dq or timestamp - self.dq[0] < 300:
            self.dq.append(timestamp)
        else:
            while self.dq and timestamp - self.dq[0] >= 300:
                self.dq.popleft()
            self.dq.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        if not self.dq or timestamp - self.dq[0] < 300:
            return len(self.dq)
        else:
            while self.dq and timestamp - self.dq[0] >= 300:
                self.dq.popleft()
            return len(self.dq)
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
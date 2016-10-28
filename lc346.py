class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque
        self.dq = deque()
        self.size = float(size)
        self.last = None
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.dq) == self.size:
            out = self.dq.popleft()
            self.dq.append(val)
            self.last += (float(val-out) / self.size)
        else:
            self.dq.append(val)
            if self.last is None:
                self.last = float(val)
            else:
                n = len(self.dq)
                self.last = (self.last * (n-1)  + val) / n
        return self.last
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
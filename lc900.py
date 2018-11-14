class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.seq = []
        for i in range(0, len(A), 2):
            if A[i] == 0:
                continue
            self.seq.append([A[i], A[i+1]])
        self.seq.reverse()

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        last_num = -1
        while self.seq and n >= self.seq[-1][0]:
            n -= self.seq[-1][0]
            last_num = self.seq[-1][1]
            self.seq.pop()
        if n > 0 and self.seq:
            self.seq[-1][0] -= n
            n = 0
            last_num = self.seq[-1][1]
        return last_num if n == 0 else -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

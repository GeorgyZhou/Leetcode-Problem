# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.cache = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        total = 0
        last = len(self.cache)
        eof = False
        if last > 0:    
            for i in xrange(min(last, n)):
                buf[i] = self.cache.pop(0)
                total += 1
        while not eof and total < n:
            tmp = ['']*4
            count = read4(tmp)
            eof = count < 4
            for i in xrange(count):
                if total < n:
                    buf[total] = tmp[i]
                    total += 1
                else:
                    self.cache.append(tmp[i])
        return total
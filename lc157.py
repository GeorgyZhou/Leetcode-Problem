# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        total = 0
        eof = False
        while not eof and total < n:
            tmp = [""]*4
            count = read4(tmp)
            eof = count < 4
            count = min(n - total, count)
            for i in xrange(0, count):
                buf[total + i] = tmp[i]
            total += count
        return total
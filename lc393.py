class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return True
        i, l = 0, len(data)
        while i < l:
            u = 128
            n = 0
            for _ in xrange(8):
                if u & data[i] != 0:
                    n += 1
                    u >>= 1
                else:
                    break
            n = max(1, n)
            if n ==  8:
                return False
            if n == 1:
                if data[i] & 128 != 0:
                    return False
            else:    
                for _ in xrange(n):
                    if data[i] & 128 != 128:
                        return False
                    data[i] <<= 1
                    data[i] &= 255
                
                if data[i] & 128 != 0:
                    return False
            for j in xrange(1, n):
                if j+i >= l or data[j+i] & 192 != 128:
                    return False
            i += n
        return True
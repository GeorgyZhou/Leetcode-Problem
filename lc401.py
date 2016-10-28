class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]
        self.nums = [800, 400, 200, 100, 32, 16, 8, 4, 2, 1]
        final = self.rec(0, num)
        # final.sort()
        for i in xrange(len(final)):
            time = str(final[i])
            if len(time) == 1:
                final[i] = '0:0' + time
            elif len(time) == 2:
                final[i] = '0:' + time
            elif len(time) == 3:
                final[i] = time[0] + ':' + time[1:]
            else:
                final[i] = time[:2] + ':' + time[2:]
        return final
    
    def rec(self, start, n):
        ret = []
        if n == 1:
            for i in xrange(start, 10):
                ret.append(self.nums[i])
            return ret
        for i in xrange(start, 10):
            for c in self.rec(i+1, n-1):
                tmp = self.nums[i] + c
                if tmp % 100 < 60 and tmp / 100 < 12:
                    ret.append(tmp)
        return ret
            
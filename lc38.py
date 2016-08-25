class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        seq = '1'
        for i in xrange(n-1):
            l = len(seq)
            count = 0
            tmp = []
            for j in xrange(l):
                if j == 0:
                    count += 1
                elif seq[j] == seq[j-1]:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(seq[j-1])
                    count = 1
            tmp.append(str(count))
            tmp.append(seq[-1])
            seq = ''.join(tmp)
            del tmp
        return seq

solution = Solution()
print solution.countAndSay(6)
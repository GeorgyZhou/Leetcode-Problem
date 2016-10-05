class Solution(object):
    def groupStrings(self, strings):
        ret = dict()
        for s in strings:
            tmp = []
            n = len(s)
            if n <= 1:
                if n in ret:
                    ret[n].append(s)
                else:
                    ret[n] = [s]
            else:
                tmp = []
                for i in xrange(1, n):
                    tmp.append((ord(s[i]) - ord(s[i-1])) % 26)
                tmp = tuple(tmp)
                print tmp
                if tmp in ret:
                    ret[tmp].append(s)
                else:
                    ret[tmp] = [s]
        return (sorted(ret.values()))

s = Solution()
s.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])

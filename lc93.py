class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []
        ret = []
        for i in xrange(0, min(4,n-2), 1):
            for j in xrange(i, min(i+4, n-1), 1):
                for k in xrange(j, min(j+4, n), 1):
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                    if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                        ret.append('.'.join([s1, s2, s3, s4]))
        return ret
    
    def isValid(self,s):
        n = len(s)
        if n == 0 or n > 3 or n > 1 and s[0] == '0':
            return False
        if 0 <= int(s) <= 255:
            return True
        else:
            return False
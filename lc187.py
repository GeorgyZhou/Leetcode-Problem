class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        dic = dict()
        if n <= 10:
            return []
        res = dict()
        for i in xrange(0,n-9,1):
            tmp = s[i:i+10]
            if dic.has_key(tmp):
                res[tmp] = 1
            else:
                dic[tmp] = 1
        return res.keys()
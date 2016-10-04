class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k == 0 or n == 0:
            return 0
        if k >= n:
            return n
        ret, start = 0, 0
        num = 0
        dic = dict()
        for i in xrange(n):
            dic[s[i]] = i
            if len(dic.keys()) > k:
                start = min(dic.values())
                del dic[s[start]]
                start += 1
            ret = max(i - start + 1, ret)
        return ret 
s = Solution()
s.lengthOfLongestSubstringKDistinct('eceba', 2)

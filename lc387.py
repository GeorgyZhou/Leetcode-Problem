class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        point = 0
        d = [0 for i in xrange(26)]
        i = 0
        while i < len(s):
            d[ord(s[i]) - ord('a')] += 1
            while point <= i and d[ord(s[point]) - ord('a')] > 1:
                point += 1
            i += 1
        return point if point < len(s) else -1

s = Solution()
print s.firstUniqChar('leetcode')
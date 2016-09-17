class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = {}
        index = 0
        pos = 0
        if not s:
            return ''
        for i in xrange(len(s)):
            cnt[s[i]] = 1 if s[i] not in cnt else cnt[s[i]] + 1
        for i in xrange(len(s)):
            if ord(s[i]) < ord(s[pos]):
                pos = i
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                break
        news = []
        for i in xrange(pos + 1, len(s)):
            if s[i] != s[pos]:
                news.append(s[i])
        # print ''.join(news)
        return s[pos] + Solution.removeDuplicateLetters(self, ''.join(news))

s = Solution()
print s.removeDuplicateLetters("cbacdcbc")


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict = {}
        total_length = 0
        for i in xrange(len(words)):
            word = words[i]
            total_length += len(word)
            if not dict[word[0]]:
                dict[word[0]] = [i]
            else:
                dict[word[0]].append(i)
        if len(s) < total_length:
            return []
        res = []
        for i in xrange(len(s) - total_length + 1):
            tmp = copy.

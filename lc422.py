class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        k = len(words)
        if k == 0:
            return False
        before = []
        for i in xrange(k):
            word = words[i]
            l = len(word)
            if l > k:
                return False
            else:
                word = word + ' ' * (k-l)
            for j in xrange(i):
                if word[j] != before[j][i]:
                    return False
            before.append(word)
        return True
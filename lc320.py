class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        n = len(word)
        if n == 0:
            return ['']
        if n == 1:
            return ['1',word]
        ret = [word]
        for i in xrange(1, n + 1):
            for j in xrange(0, n + 1 - i):
                right = self.generateAbbreviations(word[j + i + 1:])
                for r in right:
                    if j + i <= n - 1:
                        ret.append(word[:j] + str(i) + word[j+i] + r)
                    elif j + i == n:
                        ret.append(word[:j] + str(i))
        return ret
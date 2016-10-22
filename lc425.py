class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return []
        self.dic = dict()
        self.dic[''] = [word for word in words]
        for word in words:
            for i in xrange(1, len(word)):
                if word[:i] in self.dic:
                    self.dic[word[0:i]].append(word)
                else:
                    self.dic[word[0:i]] = [word]
        self.n = len(words[0])
        self.ret = []
        self.square = []
        self.rec('')
        return self.ret

    def rec(self, prefix):
        l = len(self.square)
        if prefix not in self.dic:
            return
        for word in self.dic[prefix]:
            if l < self.n - 1:
                self.square.append(word)
                self.rec(''.join([word[l+1] for word in self.square]))
                self.square.pop()
            else:
                self.ret.append([w for w in self.square] + [word])
        return

s = Solution()
print s.wordSquares(["area","lead","wall","lady","ball"])
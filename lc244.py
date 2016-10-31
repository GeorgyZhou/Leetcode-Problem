class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = dict()
        l = len(words)
        self.max = l
        for i in xrange(l):
            word = words[i]
            if word in self.dic: self.dic[word].append(i)
            else: self.dic[word] = [i]
                

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.dic[word1], self.dic[word2]
        n1, n2 = len(l1), len(l2)
        p1, p2 = 0, 0
        ret = self.max
        while p1 < n1 and p2 < n2:
            i1, i2 = l1[p1], l2[p2]
            if i1 < i2:
                ret = min(i2-i1, ret)
                p1 += 1
            else:
                ret = min(i1-i2, ret)
                p2 += 1
        return ret
        

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
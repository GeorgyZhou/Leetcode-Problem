class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        import sys
        l = len(words)
        last1, last2 = -l, -l
        distance = l
        l1 = len(word1)
        l2 = len(word2)
        for i in xrange(l):
            word = words[i]
            n = len(word)
            if n != l1 and n != l2:
                continue
            if word == word1:
                distance = min(distance, i - last2)
                last1 = i
            elif word == word2:
                distance = min(distance, i - last1)
                last2 = i
        return distance
                
        
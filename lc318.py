class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        if length <= 1:
            return 0
        bits = dict()
        for word in words:
            bits[word] = 0
            for char in word:
                bits[word] |= (1 << (ord(char) - ord('a')))
        max_product = 0
        for i in range(length-1):
            for j in range(i+1, length):
                word1, word2 = words[i], words[j]
                if bits[word1] & bits[word2] == 0:
                    max_product = max(max_product, len(word1) * len(word2))
        return max_product
        
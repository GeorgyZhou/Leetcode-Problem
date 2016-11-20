class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.n = len(sentence)
        self.lens = [len(word) for word in sentence]
        if max(self.lens) > cols:
            return 0
        word_num = self.prep(cols)
        ret, offset = 0, 0
        print word_num
        for _ in range(rows):
            num = word_num[offset]
            offset = (offset + num) % self.n
            ret += num
        return ret / self.n
    
    def prep(self, cols):
        word_num = [0 for _ in xrange(self.n)]
        for start in range(self.n):
            count = 0
            index = start
            length = self.lens[index]
            row_length = 0
            while row_length + (1 if count != 0 else 0) + length <= cols:
                row_length += (length + (1 if count != 0 else 0))
                count += 1
                index = (index + 1) % self.n
                length = self.lens[index]
            word_num[start] = count
        return word_num

s = Solution()
s.wordsTyping(["hello","world"], 2, 8)
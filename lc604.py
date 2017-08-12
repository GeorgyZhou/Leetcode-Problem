class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = compressedString
        self.index = 0
        self.count = 0
        self.letter = None

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        if self.count == 0:
            self.letter = self.string[self.index]
            self.index += 1
            while self.index < len(self.string) and ord('0') <= ord(self.string[self.index]) <= ord('9'):
                self.count = self.count * 10 + int(self.string[self.index])
                self.index += 1    
        self.count -= 1
        return self.letter
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0 or self.index < len(self.string)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
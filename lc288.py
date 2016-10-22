class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = dict()
        for w in dictionary:
            if len(w) >= 3:
                tmp = w[0] + str(len(w[1:-1])) + w[-1]
                if self.dic.has_key(tmp) and self.dic[tmp] != w:
                    self.dic[tmp] = False
                else:
                    self.dic[tmp] = w
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n < 3:
            return True
        tmp = word[0] + str(len(word[1:-1])) + word[-1]
        print tmp
        if not self.dic.has_key(tmp):
            return True
        elif self.dic[tmp] == word:
            return True
        else:
            print 'hello'
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(["hello", "heloo"])
print vwa.isUnique("heloo")
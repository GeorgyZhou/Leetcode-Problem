class ValidWordAbbr(object):
    dic = dict()
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        for dword in dictionary:
            if len(dword) >= 3:
                abbr = dword[0]+str(len(dword[0:-1]))+dword[-1]
                if abbr in self.dic:
                    self.dic[abbr] = ''
                else:
                    self.dic[abbr] = dword

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            return True
        else:
            abbr = word[0] + str(len(word[1:-1])) + word[-1]
            if abbr not in self.dic or (abbr in self.dic and self.dic[abbr] == word):
                return True
            else:
                return False


s = ValidWordAbbr([""])
print s.isUnique("")
print s.isUnique("a")
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        p1 = p2 = 0
        l1, l2 = len(word), len(abbr)
        if l1 == 0 and l2 == 0:
            return True
        if l1 == 0 or l2 == 0:
            return False
        num = []
        while p1 < l1 and p2 < l2:
            if 'a' <= abbr[p2] <= 'z':
                if len(num):
                    num = ''.join(num)
                    p1 += int(num)
                    num = []
                if p1 >= l1:
                    return False
                elif abbr[p2] == word[p1]: 
                    p1 += 1
                    p2 += 1
                else:
                    return False
            elif '0' <= abbr[p2] <= '9':
                if len(num) == 0 and abbr[p2] == '0':
                    return False
                num.append(abbr[p2])
                p2 += 1
        if len(num):
            num = ''.join(num)
            p1 += int(num)
        if p1 == l1 and p2 == l2:
            return True
        return False
        
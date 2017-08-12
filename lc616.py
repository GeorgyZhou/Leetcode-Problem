class Solution(object):
    def addBoldTag(self, s, dictionary):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bold = [False for _ in range(len(s))]
        n = len(s)
        if not n:
            return ''
        for word in dictionary:
            length = len(word)
            for i in range(0, n - length + 1):
                if s[i:i+length] == word:
                    for j in range(i, i + length):
                        bold[j] = True
        ret = []
        for i in range(n):
            if bold[i] and (i == 0 or not bold[i-1]):
                ret.append('<b>')
            ret.append(s[i])
            if bold[i] and (i == n-1 or not bold[i+1]):
                ret.append('</b>')
        return ''.join(ret)
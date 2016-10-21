class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s + ' '
        word = []
        ret = []
        for c in s:
            if c == ' ':
                if len(word) > 0:
                    ret.append(''.join(word))
                    word = []
            else:
                word.append(c)
        ret.reverse()
        return ' '.join(ret)
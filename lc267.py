class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = dict()
        part = []
        for c in s:
            if c in dic:
                del dic[c]
                part.append(c)
            else:
                dic[c] = 1
        if len(dic) > 1:
            return []
        pivot = '' if len(dic) == 0 else dic.keys()[0]
        ret = []
        part.sort()
        for per in self.permute(part):
            ret.append(''.join(per) + pivot + ''.join(reversed(per)))
        return ret
        
    def permute(self, chars):
        if len(chars) == 0:
            return [[]]
        if len(chars) == 1:
            return [chars]
        ret = []
        for i, c in enumerate(chars):
            if i == 0 or c != chars[i-1]:
                for per in self.permute(chars[:i] + chars[i+1:]):
                    per.append(c)
                    ret.append(per)
        return ret
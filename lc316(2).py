class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = dict()
        for i, char in enumerate(s):
            dic[char] = i
        ret = []
        last_index = 0
        while dic:
            min_index = min(dic.values())
            smallest = chr(ord('z') + 1)
            for i in range(last_index, min_index + 1):
                if s[i] in dic and ord(s[i]) < ord(smallest):
                    smallest = s[i]
                    last_index = i + 1
            dic.pop(smallest)
            ret.append(smallest)
            print(ret)
        return ''.join(ret)
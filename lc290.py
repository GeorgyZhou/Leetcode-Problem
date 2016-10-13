class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        start, end = 0, 0
        n = len(str)
        dic = dict()
        str += ' '
        count = 0
        l = len(pattern)
        for i in xrange(n+1):
            if count >= l:
                return False
            key = ord(pattern[count]) - ord('a')
            if str[i] == ' ' and key not in dic:
                end = i
                for k in dic:
                    if dic[k] == str[start:end]:
                        return False
                dic[key] = str[start:end]
                count += 1
                start = end + 1
            elif str[i] == ' ' and key in dic:
                end = i
                if dic[key] != str[start:end]:
                    return False
                start = end + 1
                count += 1
        if count == l:
            return True
        else:
            return False
s = Solution()
print s.wordPattern("abba", "dog cat cat dog")
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while 1:
            j = 0
            while 1:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i+j]:
                    break
                j += 1
            i += 1

solution = Solution()
print solution.strStr('123123', '231')

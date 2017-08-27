class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(reverse=True, key=lambda x: len(x))
        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i == j:
                    continue
                if self.isSubsequence(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1
    
    def isSubsequence(self, str1, str2):
        if len(str1) > len(str2):
            return False
        flag = True
        i = j = 0
        while i < len(str2) and j < len(str1):
            if str2[i] == str1[j]:
                j += 1
            i += 1
        return j == len(str1)
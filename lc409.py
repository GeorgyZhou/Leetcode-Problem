class Solution(object):
    def longestPalindrome(self, s):
        dic = dict()
        n = len(s)
        if n <= 1:
            return n
        for i in s:
            dic[i] = dic[i]+1 if dic.has_key(i) else 1
        odd = 0
        count = 0
        for i in dic.keys():
            count += dic[i]
            if dic[i] % 2 == 1:
                odd += 1
        return count if odd == 0 else count - odd + 1

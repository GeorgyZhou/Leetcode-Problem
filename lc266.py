class Solution(object):
    def canPermutePalindrome(self, s):
        n = len(s)
        if n <= 1:
            return True
        dic = dict()
        for i in s:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
        if n % 2 == 0:
            for i in dic.keys():
                if dic[i] % 2 != 0:
                    return False
            return True
        if n % 2 == 1:
            flag = False
            for i in dic.keys():
                if dic[i] % 2 != 0 and flag:
                    return False
                elif dic[i] % 2 != 0 and not flag:
                    flag = True
            return True


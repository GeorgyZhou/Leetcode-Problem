class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = dict()
        for i, char in enumerate(t):
            if char in map:
                map[char].append(i)
            else:
                map[char] = [i]
        limit = -1
        for char in s:
            if char not in map:
                return False
            flag = False
            for index in map[char]:
                if index > limit:
                    limit = index
                    flag = True
                    break
            if not flag:
                return False
        return True
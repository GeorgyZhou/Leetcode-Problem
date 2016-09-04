class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = {}
        for i in s:
            dict[i] = dict[i] + 1 if i in dict.keys() else 1
        for i in t:
            if not dict.get(i):
                return i
            else:
                dict[i] -= 1
                if dict[i] == 0:
                    del dict[i]
        return dict[dict.keys()[0]]
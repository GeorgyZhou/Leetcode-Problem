class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        if not g:
            return 0
        i = 0
        for size in s:
            if size >= g[i]:
                i += 1
                if i == len(g):
                    return i
        return i
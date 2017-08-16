class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        m, n = len(picture), len(picture[0])
        bs = set()
        dic = dict()
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if (i, -1) not in dic and (-1, j) not in dic:
                        bs.add((i, j))
                        dic[(-1, j)] = (i, j)
                        dic[(i, -1)] = (i, j)
                        continue
                    if (i, -1) in dic:
                        black = dic[(i, -1)]
                        if black in bs:
                            bs.remove(black)
                    else:
                        dic[(i, -1)] = (i, j)
                    if (-1, j) in dic:
                        black = dic[(-1, j)]
                        if black in bs:
                            bs.remove(black)
                    else:
                        dic[(-1, j)] = (i, j)
        return len(bs)
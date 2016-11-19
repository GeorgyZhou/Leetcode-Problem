class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(p1, p2):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        n = len(points)
        dic = dict()
        ret = 0
        for i in xrange(n):
            dic.clear()
            for j in xrange(n):
                if i == j:
                    continue
                d = distance(points[i], points[j])
                dic[d] = dic.get(d, 0) + 1
                ret += 2 * (dic[d] - 1)
        return ret
                
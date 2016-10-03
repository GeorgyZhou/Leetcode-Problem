class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        n = len(points)
        if n == 1 or n == 0:
            return True
        group = dict()
        for x, y in points:
            if group.has_key(y):
                group[y].add(x)
            else:
                x_set = set()
                x_set.add(x)
                group[y] = x_set
                
        mid = None
        for y in group.keys():
            xs = list(group[y])
            xs.sort()
            l, r = 0, len(xs) - 1
            while l <= r:
                if mid is None:
                    mid = xs[l] + xs[r]
                elif mid != xs[l] + xs[r]:
                    return False
                l += 1
                r -= 1
        return True


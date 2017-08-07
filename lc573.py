class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        tx, ty = tree[0], tree[1]
        sx, sy = squirrel[0], squirrel[1]
        diff = (height + width) * 5
        count = 0 
        for x, y in nuts:
            dist_t = 2 * (abs(x-tx) + abs(y-ty))
            count += dist_t
            dist_s_t = dist_t / 2 + abs(x-sx) + abs(y-sy)
            diff = min(dist_s_t - dist_t, diff)
        return count + diff
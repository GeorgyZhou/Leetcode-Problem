class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_distance = 0
        last_sitted = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                if last_sitted != -1:
                    max_distance = max(max_distance, (i - last_sitted) >> 1)
                else:
                    max_distance = max(max_distance, i)
                last_sitted = i
        last_sitted = -1
        for i, seat in enumerate(reversed(seats)):
            if seat == 1:
                if last_sitted != -1:
                    max_distance = max(max_distance, (i - last_sitted) >> 1)
                else:
                    max_distance = max(max_distance, i)
                last_sitted = i
        return max_distance

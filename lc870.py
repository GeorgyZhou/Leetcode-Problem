class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sort_a = sorted(A)
        sort_b = sorted(B)
        remaining = []
        index = 0
        map_b = {b: [] for b in set(B)}
        for a in sort_a:
            if a > sort_b[index]:
                map_b[sort_b[index]].append(a)
                index += 1
                continue
            remaining.append(a)
        return [map_b[b].pop() if map_b[b] else remaining.pop() for b in B]

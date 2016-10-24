class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        n = len(people)
        if n <= 1:
            return people
        dic = dict()
        space = [i for i in xrange(n)]
        ret = [None for _ in xrange(n)]
        heapq.heapify(people)
        while len(people) > 0:
            h, k = heapq.heappop(people)
            pos = space.pop(k-dic.get(h, 0))
            dic[h] = dic.get(h, 0) + 1
            ret[pos] = [h, k]
        return ret
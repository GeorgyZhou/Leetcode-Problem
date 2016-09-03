class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        dict = {}
        for i in nums:
            dict[i] = dict[i] + 1 if i in dict.keys() else 1

        heap = [(dict[i], i) for i in dict.keys()]
        heapq.heapify(heap)
        j = len(dict.keys()) - k
        for i in xrange(j):
            heapq.heappop(heap)
        ret = []
        for i in xrange(k):
            ret.append(heapq.heappop(heap)[1])
        return ret
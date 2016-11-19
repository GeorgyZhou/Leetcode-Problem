class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import heapq
        dic = dict()
        n = len(s)
        for i in s:
            dic[i] = dic.get(i, 0) - 1
        heap = dic.items()
        heap.sort(reverse=True, key=lambda x: x[1])
        ret = []
        print heap
        while len(heap) > 0:
            c, num = heap.pop()
            ret.append(c*(-num))
        return ''.join(ret)
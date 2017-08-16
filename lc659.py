class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import heapq
        import collections
        if len(nums) < 3:
            return False
        ends = collections.defaultdict(list)
        insuf = 0
        for num in nums:
            if num-1 in ends:
                count = heapq.heappop(ends[num-1])
                if len(ends[num-1]) == 0:
                    del ends[num-1]
                heapq.heappush(ends[num], count + 1)
                if count == 2:
                    insuf -= 1
            else:
                heapq.heappush(ends[num], 1)
                insuf += 1
        return insuf == 0
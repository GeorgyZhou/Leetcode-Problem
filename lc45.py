class Solution(object):

    def jump(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """
        n = len(nums)
        if n <= 1:
            return 0
        count = 0
        start,end = 0, nums[0]
        while end < n - 1:
            mv, mi = 0, 0
            for i in xrange(start, end+1):
                if nums[i] + i > mv:
                    mv = nums[i] + i
                    mi = i
            start = end + 1
            end = mv
            count += 1
        count += 1
        return count

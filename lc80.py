class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        length = 0
        count = 0
        lastnum = None
        delete = []
        for i in xrange(len(nums)):
            num = nums[i]
            if lastnum is None or lastnum != num:
                count = 1
                lastnum = num
                length += 1
                if len(delete) > 0:
                    nums[delete[0]] = num
                    del delete[0]
                    delete.append(i)
            elif lastnum == num and count < 2:
                count += 1
                length += 1
                if len(delete) > 0:
                    nums[delete[0]] = num
                    del delete[0]
                    delete.append(i)
            else:
                delete.append(i)
        return length
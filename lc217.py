class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = dict()
        for num in nums:
            if num in dic:
                return True
            dic[num] = 1
        return False
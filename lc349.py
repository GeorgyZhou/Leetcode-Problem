class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        ret = []
        for num in nums1:
            dic[num] = 1
        for num in nums2:
            if num in dic:
                del dic[num]
                ret.append(num)
        return ret
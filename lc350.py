class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        ret = []
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        for num in nums2:
            if dic.get(num, 0) > 0:
                dic[num] -= 1
                ret.append(num)
        return ret
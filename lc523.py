class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_dic = dict()
        sum_dic[0] = -1
        count = 0
        s = 0
        for i in range(len(nums)):
            num = nums[i]
            s += num
            if k != 0:
                s %= k
            if s in sum_dic:
                if i - sum_dic[s] > 1: 
                    return True
            sum_dic[s] = sum_dic.get(s, i)
        return False
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i in xrange(len(numbers)):
            if dic.has_key(numbers[i]):
                return [dic[numbers[i]], i+1]
            dic[target - numbers[i]] = i+1
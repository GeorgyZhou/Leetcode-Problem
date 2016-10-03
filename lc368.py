class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        nums.sort()
        dp = [1 for _ in xrange(n)]
        parent = dict()
        for i in xrange(1, n):
            length = 1
            for j in xrange(0,i):
                if nums[i] % nums[j] == 0:
                    if length  < dp[j] + 1:
                        length = dp[j] + 1
                        parent[i] = j
                        dp[i] = dp[j] + 1
        max_num = 0
        ret = []
        for i in xrange(n):
            if dp[i] > max_num:
                ret = []
                max_num = dp[i]
                ret = [nums[i]]
                cur = i
                while parent.has_key(cur):
                    cur = parent[cur]
                    ret.append(nums[cur])
        return ret

s= Solution()
print s.largestDivisibleSubset([3,4,16,8])



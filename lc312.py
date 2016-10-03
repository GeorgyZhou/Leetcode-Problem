class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return nums[0] * nums[1] + max(nums[0], nums[1])
        nums = [1] + nums + [1]
        l += 2
        self.dp = [[0 for _ in xrange(l)] for i in xrange(l)]
        return self.recur(nums, 0, l-1)

    def recur(self, nums, i, j):
        print i, j
        if self.dp[i][j] != 0 or i + 1 == j:
            return self.dp[i][j]
        else:
            ans = 0
            for k in xrange(i+1, j):
                ans = max(ans, nums[k] * nums[i] * nums[j] + self.recur(nums, i, k) + self.recur(nums, k, j))
            self.dp[i][j] = ans
        return self.dp[i][j]

sol = Solution()
print sol.maxCoins([1,6,8,3,4,6,4,7,9,8,0,6,2,8])


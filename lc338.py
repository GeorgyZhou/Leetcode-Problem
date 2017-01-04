class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dp = [0 for _ in range(num+1)]
        dp[0] = 0
        bound = 2
        for number in range(1, num+1):
            if number == bound:
                dp[number] = 1
                bound *= 2
            else:
                dp[number] = dp[number - bound / 2] + 1
        return dp
            
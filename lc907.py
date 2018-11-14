class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        left_min = []
        right_min = []
        prev_min = []
        next_min = [None for _ in range(len(A))]
        for index in range(len(A)):
            while left_min and A[index] <= A[left_min[-1]]:
                left_min.pop()
            prev_min.append(left_min[-1] if left_min else -1)
            left_min.append(index)
        for index in range(len(A) - 1, -1, -1):
            while right_min and A[index] < A[right_min[-1]]:
                right_min.pop()
            next_min[index] = right_min[-1] if right_min else len(A)
            right_min.append(index)
        ans = 0
        for index, value in enumerate(A):
            ans += (next_min[index] - index) * (index -  prev_min[index]) * value
            ans %= MOD
        return ans

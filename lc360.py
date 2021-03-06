class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        n = len(nums)
        if n == 0:
            return []
        ret = []
        if a == 0 and b < 0:
            for i in xrange(n-1, -1, -1):
                ret.append(self.func(a, b, c, nums[i]))
            return ret
        elif a == 0 and b >= 0:
            for i in xrange(n):
                ret.append(self.func(a, b, c, nums[i]))
            return ret
        left, right = 0, n-1
        pivot = - float(b) / (2.0 * float(a))
        while left <= right:
            if abs(nums[right] - pivot) > abs(nums[left] - pivot):
                ret.append(self.func(a, b, c, nums[right]))
                right -= 1
            else:
                ret.append(self.func(a, b, c, nums[left]))
                left += 1
        if a > 0:
            ret.reverse()
        return ret

    def func(self, a, b, c, num):
        return a * num * num + b * num + c


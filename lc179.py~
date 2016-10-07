class Solution:
    def largestNumber(self, nums):
        return map(lambda x: x if x else '0',[''.join(sorted(map(str,nums), cmp=lambda x,y: cmp(y+x, x+y))).lstrip('0')])[0]

s = Solution()
print s.largestNumber([0,0])

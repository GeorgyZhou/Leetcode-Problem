class Solution(object):
    def addParenthesis(self, ans, str, left, right):
        if left > right:
            return
        if left > 0:
            Solution.addParenthesis(self, ans, str + '(', left - 1, right)
        if right > 0:
            Solution.addParenthesis(self, ans, str + ')', left, right - 1)
        if not right and not left:
            ans.append(str)
            return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        ans = []
        left, right, str = n, n, ''
        Solution.addParenthesis(self, ans, str, left, right)
        return ans

solution = Solution()
r = solution.generateParenthesis(4)
for x in r:
    print x
print len(r)

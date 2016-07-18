class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            print stack
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and len(stack) >= 1 and stack[-1] == '(':
                del stack[-1]
            elif i == ']' and len(stack) >= 1 and stack[-1] == '[':
                del stack[-1]
            elif i == '}' and len(stack) >= 1 and stack[-1] == '{':
                del stack[-1]
            else:
                return False
        if len(stack) == 0:
            return True
        return False

solution = Solution()
print solution.isValid("]")
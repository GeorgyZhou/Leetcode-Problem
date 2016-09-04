class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder += ','
        stack = []
        point = 0
        condition = []
        if preorder == '#,':
            return True
        for i in xrange(len(preorder)):
            if preorder[i] == ',':
                if preorder[point:i] == '#':
                    if len(condition) == 0:
                        return False
                    condition[-1] += 1
                    while condition[-1] == 2:
                        del condition[-1]
                        del stack[-1]
                        if len(condition) == 0:
                            if i == len(preorder) - 1:
                                return len(stack) == 0
                            else:
                                return False
                        condition[-1] += 1
                else:
                    stack.append(preorder[point:i])
                    condition.append(0)
                point = i + 1
        return len(stack) == 0


s = Solution()
print s.isValidSerialization("1,#")
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ''
        ret = []
        stack = []
        tmp = 0
        for i in xrange(n):
            if '0' <= s[i] <= '9':
                tmp = tmp * 10 + int(s[i]) 
            elif s[i] == ']':
                cur = stack[-1]
                del stack[-1]
                repeat = cur[0]
                del cur[0]
                strings = ''.join(cur)
                strings = ''.join([strings for _ in xrange(repeat)])
                if len(stack) == 0:
                    ret.append(strings)
                else:
                    stack[-1].append(strings)
            elif s[i] != '[':
                if len(stack) > 0:
                    stack[-1].append(s[i])
                else:
                    ret.append(s[i])
            elif s[i] == '[':
                stack.append([tmp])
                tmp = 0
        return ''.join(ret)

s = Solution()
print s.decodeString("2[abc]0[cd]ef")           

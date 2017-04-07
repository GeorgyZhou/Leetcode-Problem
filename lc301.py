class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res1 = [""]
        res2 = [""]
        self.validParentheses(s, res1)
        self.validParentheses(s,reverse(), res2)
        print res1
        print res2
        return res1 + res2
        
    def validParentheses(self, s, res):
        acc = 0
        start = 0
        indexes = list()
        for i, c in enumerate(s):
            if c == "(":
                acc += 1
            elif c == ")":
                indexes.append(i)
                acc -= 1
            if acc < 0:
                last = None
                next = []
                for index in indexes:
                    if not last or index != last + 1:
                        last = index
                        for pre in res:
                            next.append(pre + s[start:index] + s[index+1:i+1])
                        res = next
                        print res
                start = i + 1
                indexes = []  
                acc += 1

if __name__ == "__main__":
    s = Solution()
    print s.removeInvalidParentheses("()())()")
                        
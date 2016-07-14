dict = {}
dict['1'] = []
dict['2'] = ['a', 'b', 'c']
dict['3'] = ['d', 'e', 'f']
dict['4'] = ['g', 'h', 'i']
dict['5'] = ['j', 'k', 'l']
dict['6'] = ['m', 'n', 'o']
dict['7'] = ['p', 'q', 'r', 's']
dict['8'] = ['t', 'u', 'v']
dict['9'] = ['w', 'x', 'y', 'z']
dict['0'] = [' ']

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        if len(digits) == 0:
            return res
        if len(digits) == 1:
            return dict[digits[0]]
        else:
            for i in dict[digits[0]]:
                for x in Solution.letterCombinations(self, digits[1:len(digits)]):
                    res.append(i + x)
        return res

solution = Solution()
print solution.letterCombinations("23")

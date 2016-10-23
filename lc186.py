class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        start = 0
        end = 0
        n = len(s)
        for i in xrange(n):
            if s[i] == ' ':
                end = i
                self.reverse(s, start, i)
                start = i+1
        self.reverse(s, start, n)
        self.reverse(s, 0, n)
    
            
    def reverse(self, s, i, j):
        for index in xrange(i, i + (j-i) / 2):
            tmp = s[index]
            s[index] = s[j - index + i - 1]
            s[j-index+i-1] = tmp
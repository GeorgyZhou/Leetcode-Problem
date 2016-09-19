class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        left = []
        right = []
        letter = {'a':1, 'e':1, 'o':1, 'i':1, 'u':1, 'A':1, 'E':1, 'O':1, 'I':1, 'U':1}
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in letter and s[r] in letter:
                left.append(s[r])
                right.append(s[l])
                l += 1
                r -= 1
            elif s[l] in letter:
                right.append(s[r])
                r -= 1
            elif s[r] in letter:
                left.append(s[l])
                l += 1
            else:
                left.append(s[l])
                right.append(s[r])
                r -= 1
                l += 1
        if l == r:
            left.append(s[r])
        right.reverse()
        return ''.join(left) + ''.join(right)

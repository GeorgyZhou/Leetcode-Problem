class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        left, right = 0 , n-1
        while left < n and not ('0' <= s[left] <= '9' or 'a' <= s[left] <= 'z' or 'A' <= s[left] <= 'Z'):
            left += 1
        while right >= 0 and not ('0' <= s[right] <= '9' or 'a' <= s[right] <= 'z' or 'A' <= s[right] <= 'Z'):
            right -= 1
        while left <= right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                while right >= 0 and not ('0' <= s[right] <= '9' or 'a' <= s[right] <= 'z' or 'A' <= s[right] <= 'Z'):
                    right -= 1
                while left < n and not ('0' <= s[left] <= '9' or 'a' <= s[left] <= 'z' or 'A' <= s[left] <= 'Z'):
                    left += 1
            else:
                return False
        return True
        
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        is_lower = 'a' <= word[0] <= 'z'
        is_upper = False
        for i in xrange(1, len(word)):
            if 'A' <= word[i] <= 'Z':
                if is_lower:
                    return False
                else:
                    is_upper = True
            if 'a' <= word[i] <= 'z':
                if is_upper:
                    return False
                else:
                    is_lower = True
        return True
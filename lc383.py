class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = [0 for i in xrange(26)]
        for i in magazine:
            dict[ord(i) - ord('a')] += 1
        for j in ransomNote:
            if dict[ord(j) - ord('a')] == 0:
                return False
            dict[ord(j) - ord('a')] -= 1
        return True
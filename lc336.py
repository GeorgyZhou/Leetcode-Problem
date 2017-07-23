class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left <= right:
                if (s[left] != s[right]):
                    return False
                left += 1
                right -= 1
            return True
        ret = []
        dic = dict()
        reverse_dic = dict()
        for i, word in enumerate(words):
            dic[word] = i
            reverse_dic[word[::-1]] = i
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                if prefix in reverse_dic and reverse_dic[prefix] != i and isPalindrome(word[j:]) and j != len(word):
                    ret.append([i, reverse_dic[prefix]])
            reverse_word = word[::-1]
            for j in range(len(reverse_word)+1):
                prefix = reverse_word[:j]
                if prefix in dic and dic[prefix] != i and isPalindrome(reverse_word[j:]):
                    ret.append([dic[prefix], i])
        return ret
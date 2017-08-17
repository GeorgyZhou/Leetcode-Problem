class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        import collections
        index_dic = collections.defaultdict(list)
        for i, char in enumerate(s):
            index_dic[char].append(i)
        longest = 0
        ret = ""
        for word in d:
            flag = True
            last_index = -1
            for char in word:
                if char not in index_dic or last_index >= index_dic[char][-1]:
                    flag = False
                    break
                for i in index_dic[char]:
                    if i > last_index:
                        last_index = i
                        break
            if flag:
                if len(word) > longest:
                    longest = len(word)
                    ret = word
                elif len(word) == longest:
                    for i in xrange(longest):
                        if word[i] < ret[i]:
                            ret = word
                            break
                        elif word[i] > ret[i]:
                            break
        return ret
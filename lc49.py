class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for word in strs:
            maps = [0 for _ in xrange(26)]
            for ch in word:
                maps[ord(ch) - ord('a')] += 1
            maps = tuple(maps)
            if dic.has_key(maps):
                dic[maps].append(word)
            else:
                dic[maps] = [word]
        
        return dic.values()
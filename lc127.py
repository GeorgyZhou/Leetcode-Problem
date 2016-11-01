class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def ladder(str1, str2):
            if len(str1) != len(str2):
                return False
            flag = True
            for i in xrange(len(str1)):
                if str1[i] != str2[i]:
                    if flag: flag = False
                    else: return False
            return not flag
        
        sused, eused = dict(), dict()
        start, end = [(beginWord,1)], [(endWord,1)]
        while len(start) > 0 and len(end) > 0:
            (sn, sl), (en, el) = start[0], end[0]
            del start[0], end[0]
            if en in sused:
                return el + sused[en] - (1 if sn == en else 2)
            if sn in eused:
                return eused[sn] + sl - (1 if sn == en else 2)
            sused[sn], eused[en] = sl, el 
            for word in wordList:
                if word not in eused and ladder(word, en):
                    end.append((word, el+1))
                if word not in sused and ladder(word, sn):
                    start.append((word, sl+1))
        return 0
s = Solution()
print s.ladderLength("cost", "lost", set(["lost","cost","most"]))
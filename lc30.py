class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        wl = len(words[0])
        ans = []

        for k in xrange(wl):
            left = k
            subd = {}
            count = 0
            for j in xrange(k, len(s) - k + 1, wl):
                tword = s[j:j+wl]
                if tword in dict:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    # push the window
                    while subd[tword] > dict[tword]:
                        subd[s[left:left+wl]] -= 1
                        count -= 1
                        left += wl
                    if count == len(words):
                        ans.append(left)
                else:
                    count = 0
                    left = j + wl
                    subd = {}
        return ans


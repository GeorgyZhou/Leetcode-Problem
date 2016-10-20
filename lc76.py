class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import sys
        ls, lt = len(s), len(t)
        if ls == 0 or lt == 0:
            return 0
        dic = dict()
        need = lt
        for i in t:
            dic[i] = dic[i] + 1 if i in dic else 1
        begin = end = head = 0
        d = sys.maxint
        while end < ls:
            if s[end] in dic:
                if dic[s[end]] > 0:
                    need -= 1
                dic[s[end]] -= 1
            end += 1
            while need == 0:
                if (end - begin) < d:
                    d = end -begin
                    head = begin
                if s[begin] not in dic:
                    begin += 1
                elif s[begin] in dic:
                    if dic[s[begin]] == 0:
                        need += 1
                    dic[s[begin]] += 1
                    begin += 1
        return '' if d == sys.maxint else s[head:head+d]
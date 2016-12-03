class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        n = len(target)
        for i in xrange(len(dictionary)):
            if len(dictionary[i]) != n:
                del dictionary[i]
        if n == 0:
            return "0" if "" not in dictionary else ""
        abbrs = self.find_abbr(target)
        # print abbrs
        for abbr in abbrs: 
            if self.is_valid(dictionary, abbr):
                return abbr
        return None
        
    def is_valid(self, dictionary, abbr):
        parse = []
        num = ""
        length = 0
        if abbr == "1p3":
            pass
        n = len(dictionary)
        for c in abbr:
            if "1" <= c <= "9":
                num += c
            else:
                if num != "":
                    parse.append(int(num))
                    length += int(num)
                    num = ""
                parse.append(c)
                length += 1
        if num != "":
            parse.append(int(num))
            length += int(num)
        flag = 0
        for word in dictionary:
            i = 0
            lock = False
            while i < length:
                for j in parse:
                    if isinstance(j, str):
                        if word[i] != j and not lock:
                            flag += 1
                            lock = True
                        i += 1
                    elif isinstance(j, int):
                        i += j
        return flag == n
                
    
    def find_abbr(self, target):
        if not target:
            return [target]
        n = len(target)
        ret = []
        for i in xrange(n, 0, -1):
            for j in xrange(0, n-i+1):
                left = self.find_abbr(target[:(j-1 if j >= 1 else 0)])
                right = self.find_abbr(target[i+j+1:])
                for l in left:
                    for r in right:
                        abbr = l + (target[j-1] if j != 0 else "") + str(i) + (target[i+j] if i+j < n else "") + r
                        ret.append(abbr)
        ret.append(target)
        return ret

s = Solution()
print s.minAbbreviation("apple", ["plain", "amber", "blade"])
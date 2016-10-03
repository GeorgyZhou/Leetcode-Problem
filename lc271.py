class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        ret = []
        num = []
        for i in strs:
            ret.append(i)
            num.append(',' + str(len(i)))
        if len(num) > 0:
            num.append(',')
        ret.append(''.join(num))
        ret.append(str(len(strs)))
        return ''.join(ret)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        ret = []
        if len(s) > 0:
            lenght = 0
            for i in xrange(len(s)-1, -1, -1):
                if s[i] == ',':
                    length = int(s[i+1:len(s)])
                    break
        else:
            return []
        current = 0
        sublength = []
        count = 0
        last_comma = len(s)

        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == ',':
                count += 1
                if last_comma != len(s):
                    sublength.append(int(s[i+1:last_comma]))
                last_comma = i
                if count == length + 1:
                    break
        sublength.reverse()

        for i in xrange(length):
            ret.append(s[current:current+sublength[i]])
            current += sublength[i]
        return ret


        # Your Codec object will be instantiated and called as such:
strings = ["1111111111111111111111111","2222222222222222222222222222222222222222222222222","333333333333333333333333333333","4444","555555555555555555555555555555555555555","666","777777777","8888888888888","99999999999999999999999999999999999999999999","U;P N[rokvXh(E9k2=?7`/ Cyc8!HM+av1AVNm5f=<.?ak+Sac>e?h8ob|h)U?bU{@;$a7w7Fr","y`g,n.Z1J81; ;VH!s`V5U?iAl)owoRc#UC2(~[x*Eoq|5vghwtbvq&lV?w nQv?s#&q6~d}@wM","O}r+9|M9u}x;VIn;Zmw{*Fj-CV,yaGa%Yg9-H|n=Saipfti4O(,n^#RLfhAE=%At[bRzNm$hIPQf=Vi }#kk8U7"]
codec = Codec()
print codec.decode(codec.encode(strings))
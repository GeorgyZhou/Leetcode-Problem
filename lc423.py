class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = dict()
        dic = dict()
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        if 'z' in dic:
            num = dic.get('z')
            res['0'] = num
            dic['z'] = 0
            dic['o'] -= num
        if 'w' in dic:
            num = dic.get('w')
            res['2'] = num
            dic['o'] -= num
        if 'u' in dic:
            num = dic.get('u')
            res['4'] = num
            dic['f'] -= num
            dic['o'] -= num
        if 'x' in dic:
            num = dic.get('x')
            res['6'] = num
            dic['i'] -= num
            dic['s'] -= num
        if 's' in dic:
            num = dic.get('s')
            res['7'] = num
        if 'g' in dic:
            num = dic.get('g')
            res['8'] = num
            dic['i'] -= num
            dic['h'] -= num
        if 'o' in dic:
            res['1'] = dic.get('o')
        if 'h' in dic:
            res['3'] = dic.get('h')
        if 'f' in dic and dic['f'] != 0:
            num = dic.get('f')
            res['5'] = num
            dic['i'] -= num
        if 'i' in dic:
            res['9'] = dic.get('i')
        ret = ''
        for i in range(10):
            ret += str(i) * res.get(str(i), 0)
        return ret
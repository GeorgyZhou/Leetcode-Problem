class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'6':'9', '9':'6', '0':'0', '8':'8', '1':'1'}
        new_str = []
        for i in xrange(len(num)-1, -1, -1):
            if dic.has_key(num[i]):
                new_str.append(dic[num[i]])
            else:
                return False 
        new_str = ''.join(new_str)
        if new_str == num:
            return True
        return False

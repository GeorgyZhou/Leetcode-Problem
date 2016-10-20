class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        for i in path.split('/'):
            if i == '.' or i == '':
                continue
            elif i == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(i)
        return '/' + '/'.join(res)
            
        
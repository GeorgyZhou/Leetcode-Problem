class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for path in paths:
            split_path = path.split(' ')
            directory, files = split_path[0], split_path[1:]
            for file in files:
                file_split = file.split('(')
                file_name = '('.join(file_split[:-1])
                file_content = file_split[-1][:-1]
                if file_content not in dic:
                    dic[file_content] = []
                dic[file_content].append(directory + '/' + file_name)
        ret = []
        for content in dic:
            if len(dic[content]) > 1:
                ret.append(dic[content])
        return ret
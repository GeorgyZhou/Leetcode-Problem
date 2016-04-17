class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if strs[0] == "":
            return ""
        common_prefix = strs[0]
        i = 0
        while(i < len(strs)):
            if strs[i][0:len(common_prefix)] == common_prefix:
                i = i + 1
            else:
                common_prefix = common_prefix[0:len(common_prefix) - 1]
        return common_prefix
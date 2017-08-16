class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        chars = [1]
        count = 0
        cur_pos = 0
        cur_num = 1
        one_num = 1
        while len(chars) < n:
            if count == 0:
                cur_num = 3 - cur_num
                chars.append(cur_num)
                cur_pos += 1
                count = chars[cur_pos] - 1
            else:
                count -= 1
                chars.append(cur_num)
        return 2 * len(chars) - sum(chars)
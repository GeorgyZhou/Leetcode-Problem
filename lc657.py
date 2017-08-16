class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h, v = 0, 0
        for move in moves:
            if move == 'L':
                h -= 1
            elif move == 'R':
                h += 1
            elif move == 'U':
                v += 1
            elif move == 'D':
                v -= 1
        return h == 0 and v == 0
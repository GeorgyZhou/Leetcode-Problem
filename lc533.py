class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0
        m, n = len(picture), len(picture[0])
        row = [0 for _ in range(m)]
        col = [[0, ''] for _ in range(n)]
        for i in range(m):
            row_code = ''.join(picture[i])
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    if col[j][0] > 0:
                        if row_code == col[j][1]:
                            col[j][0] += 1
                        else:
                            col[j][0] = -1
                    elif col[j][0] == 0:
                        col[j][0] += 1
                        col[j][1] = row_code
        count = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and col[j][0] == N and row[i] == N:
                    count += 1
        return count
                    
                
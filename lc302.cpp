class Solution {
public:
    int minArea(vector<vector<char>>& image, int x, int y) {
        int m = image.size();
        if (m == 0) return 0;
        int n = image[0].size();
        int minRow = m, minCol = n, maxRow = -1, maxCol = -1;
        for (int i = 0, j; i < m; i++) {
            for (j = 0; j < n; j++) {
                if (image[i][j] == '1') {
                    minRow = min(minRow, i);
                    minCol = min(minCol, j);
                    maxRow = max(maxRow, i);
                    maxCol = max(maxCol, j);
                }
            }
        }
        cout << minRow << minCol << maxRow << maxCol << endl;
        if (minRow == m || minCol == n || maxRow == -1 || maxCol == -1) return 0;
        return (maxRow - minRow + 1) * (maxCol - minCol + 1);
    }
};
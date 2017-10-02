class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        if (M.size() == 0 || M[0].size() == 0) return {{}};
        int ar[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
        int ac[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
        for (int i = 0, j; i < M.size(); i++) {
            for (j = 0; j < M[0].size(); j++) {
                int cnt = 1, sum = M[i][j];
                for (int k = 0; k < 8; k++) {
                    int x = i + ar[k], y = j + ac[k];
                    if (x < 0 || x >= M.size() || y < 0 || y >= M[0].size()) continue;
                    cnt++;
                    sum += M[x][y] & 0xFF;
                }
                M[i][j] |= (sum/cnt << 8);
            }
        }
        for (int i = 0; i < M.size(); i++)
            for (int j = 0; j < M[0].size(); j++) 
                M[i][j] >>= 8;
        return M;
    }
};
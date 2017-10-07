class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return {};
        vector<vector<int>> tri;
        tri.push_back({1});
        for (int i = 1, j; i < numRows; i++) {
            tri.push_back({});
            for (j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    tri[i].push_back(tri[i-1][j == 0 ? 0 : j-1]);
                    continue;
                }
                tri[i].push_back(tri[i-1][j-1] + tri[i-1][j]);
            }
        }
        return tri;
    }
};
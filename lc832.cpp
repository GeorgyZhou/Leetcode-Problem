class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for (auto& line : A) {
          int i = 0, n = line.size();
          int tmp = 0;
          while (i <= n - 1 - i) {
            tmp = 1 - line[i];
            line[i] = 1 - line[n-1-i];
            line[n-1-i] = tmp;
            ++i;
          }
        }
        return A;
    }
};

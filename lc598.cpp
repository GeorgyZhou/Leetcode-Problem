class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int size = ops.size(), x = m, y = n;
        for (int i = 0; i < size; i++) {
            x = min(x, ops[i][0]);
            y = min(y, ops[i][1]);
        }
        return x * y;
    }
};
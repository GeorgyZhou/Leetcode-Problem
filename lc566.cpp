class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size();
        if (m == 0) return nums;
        int n = nums[0].size();
        if (m * n != r * c) return nums;
        vector<vector<int>> ret(r, vector<int>(c, 0));
        for (int i = 0, j, k; i < m; i++) {
            for (j = 0; j < n; j++) {
                k = i * n  + j;
                ret[k / c][k % c] = nums[i][j];
            }
        }
        return ret;
    }
};
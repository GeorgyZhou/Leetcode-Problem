class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        int sums[n];
        sums[0] = nums[0];
        dp.resize(n, vector<int>(m, INT_MAX));
        for (int i = 1; i < n; ++i) sums[i] = sums[i-1] + nums[i];
        for (int i = 0; i < n; ++i) dp[i][0] = sums[i];
        for (int i = 0; i < n; ++i) {
            int parts = min(m, i+1);
            for (int k = 1; k < parts; ++k) {
                for (int j = i; j >= k; --j) {
                    int sum = sums[i] - sums[j] + nums[j];
                    if (sum > dp[i][k]) break;
                    dp[i][k] = min(dp[i][k], max(sum, dp[j-1][k-1]));
                }
            }
        }
        return dp[n-1][m-1];
        
    }
private:
    vector<vector<int>> dp;
};
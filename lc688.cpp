class Solution {
public:
    double knightProbability(int N, int K, int r, int c) {
        vector<vector<vector<double>>> dp(K+1, vector<vector<double>>(N, vector<double>(N, -1.0)));
        return dfs(dp, N, K, r, c);
    }
private:
    int ac[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
    int ar[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
    double dfs(vector<vector<vector<double>>>& dp, int n, int k, int r, int c) {
        if (r < 0 || r >= n || c < 0 || c >= n) return 0.0;
        if (dp[k][r][c] != -1.0) return dp[k][r][c];
        if (k == 0) return 1.0;
        double ans = 0.0;
        for (int i = 0; i < 8; i++) {
            ans += dfs(dp, n, k-1, r + ar[i], c + ac[i]) / 8.0;
        }
        dp[k][r][c] = ans;
        return ans;
    }
};
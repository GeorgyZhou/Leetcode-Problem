class Solution {
public:
    int strangePrinter(string s) {
        int n = s.size();
        if (n <= 1) return n;
        int dp[n+1][n];
        for (int i = 0; i <= n; ++i) { 
            for (int j = 0; j < n; ++j) {
                dp[i][j] = i < j ? INT_MAX : (i == j ? 1 : 0);
            }
        }
        for (int k = 1; k < n; ++k) {
            for (int i = 0; i < n - k; ++i) {
                dp[i][i+k] = dp[i+1][i+k] + 1;
                for (int j = i + 1; j <= i + k; ++j) {
                    if (s[j] == s[i]) {
                        dp[i][i+k] = min(dp[i][j-1] + dp[j+1][i+k], dp[i][i+k]);
                    } 
                }
            }
        }
        return dp[0][n-1];
    }
};
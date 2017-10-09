class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        int ret = 0;
        if (n == 0) return 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) 
            dp[i][i] = 1;
        for (int i = n-2; i >= 0; i--) {
            for (int j = i+1; j < n; j++) {
                if (s[i] == s[j]) {
                    dp[i][j] = max(max(dp[i+1][j], dp[i][j-1]), dp[i+1][j-1] + 2);
                } else {
                    dp[i][j] = max(max(dp[i+1][j], dp[i][j-1]), dp[i+1][j-1]);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                ret = max(ret, dp[i][j]);
            }
        }
        return ret;
    }
};
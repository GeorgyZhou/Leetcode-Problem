class Solution {
public:
    int integerBreak(int n) {
        int dp[n+1] = {0};
        dp[2] = 1;
        for (int i = 3; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = max((i-j) * j, max(dp[i-j] * j, dp[i]));
            }
        }
        return dp[n];
    }
};
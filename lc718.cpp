class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        if (m == 0 || n == 0) return 0;
        int dp[m+1][n+1] = {0};
        int res = 0;
        for (int i = 0; i < m; i++) dp[i][0] = 0;
        for (int i = 0; i < n; i++) dp[0][i] = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (A[i-1] == B[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    res = max(dp[i][j], res);
                } else {
                    dp[i][j] = 0;
                }
            }
        }
        return res;
    }
};
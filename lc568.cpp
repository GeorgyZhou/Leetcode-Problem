class Solution {
public:
    int maxVacationDays(vector<vector<int>>& flights, vector<vector<int>>& days) {
        int m = flights.size(), n = days[0].size();
        int dp[m][n] = {0};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) dp[i][j] = 0;
            dp[i][n-1] = days[i][n-1];
        }
        for (int k = n-2; k >= 0; --k) {
            for (int i = 0; i < m; i++) {
                dp[i][k] = dp[i][k+1] + days[i][k];
                for (int j = 0; j < m; j++) {
                    if (flights[i][j]) {
                        dp[i][k] = max(dp[i][k], dp[j][k+1] + days[i][k]);
                    }
                }
            }
        }
        int res = 0;
        for (int i = 0; i < m; ++i) {
            if(flights[0][i] || i == 0) res = max(dp[i][0], res);
        }
        return res;
    }
};
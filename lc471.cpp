class Solution {
public:
    string encode(string s) {
        int n = s.size();
        vector<vector<string>> dp(n, vector<string>(n));
        for (int l = 1; l <= n; ++l) {
            for (int i = 0; i < n - l + 1; ++i) {
                int j = i + l - 1;
                string ss = s.substr(i, l);
                dp[i][j] = ss;
                for (int k = i; k < j; k++) {
                    string left = dp[i][k];
                    string right = dp[k+1][j];
                    if (left.size()  + right.size() < dp[i][j].size()) dp[i][j] = left + right;
                }
                int pos = (ss + ss).find(ss, 1);
                string replace = (pos >= ss.size() ? ss : to_string(ss.size() / pos) + "[" + dp[i][i + pos - 1] + "]");
                if (replace.size() < dp[i][j].size()) dp[i][j] = replace;
            }
        }
        return dp[0][n-1];
    }
};1
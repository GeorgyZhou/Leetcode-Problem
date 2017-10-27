class Solution {
public:
    int findSubstringInWraproundString(string p) {
        int n = p.size();
        if (n == 0) return 0;
        int dp[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            if (i > 0 && (26 + p[i] - p[i-1]) % 26 == 1)
                dp[i] += dp[i-1];
            cout << dp[i] << endl;
        }
        int sum = 0;
        unordered_map<char, int> dic;
        for (int i = 0; i < n; i++) {
            if (dic.find(p[i]) != dic.end()) {
                sum += max(0, dp[i] - dic[p[i]]);
                dic[p[i]] = max(dic[p[i]], dp[i]);
            } else {
                dic[p[i]] = dp[i];
                sum += dp[i];
            }
        }
        return sum;
    }
};
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        auto cmp = [] (vector<int> v1, vector<int> v2) {
            return v1[0] == v2[0] ? v1[1] < v2[1] : v1[0] < v2[0]; 
        };
        sort(pairs.begin(), pairs.end(), cmp);
        vector<int> dp(n, 1);
        for (int i = 1, j; i < n; i++) {
            for (j = 0; j < i; j++) {
                if (pairs[j][1] < pairs[i][0]) {
                    dp[i] = max(dp[j] + 1, dp[i]);
                }
            }
        }
        int maximum = 0;
        for (int i = 0; i < n; i++) {
            maximum = max(dp[i], maximum);
        }
        return maximum;
    }
};
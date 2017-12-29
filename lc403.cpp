class Solution {
public:
    bool canCross(vector<int>& stones) {
        int n = stones.size();
        if (n <= 1) return true;
        vector<unordered_set<int>> dp(n, unordered_set<int>());
        dp[0] = {1};
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int step = stones[i] - stones[j]; 
                if (dp[j].find(step) == dp[j].end()) continue;
                dp[i].insert(step);
                dp[i].insert(step + 1);
                dp[i].insert(step - 1);
            }
        }
        return dp[n-1].size() > 0;
    }
};
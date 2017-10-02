class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        size_t len = nums.size();
        if (len == 0) return 0;
        vector<pair<int, int>> dp;
        for (int i = 0; i< len; i++)
            dp.push_back(make_pair(1, 1));
        for (int i = 1, j; i < len; i++) {
            for (j = 0; j < i; j++) {
                if (nums[i] <= nums[j]) continue;
                if (dp[j].first + 1 == dp[i].first) {
                    dp[i].second += dp[j].second;
                } else if (dp[j].first + 1 > dp[i].first) {
                    dp[i] = make_pair(dp[j].first + 1, dp[j].second); 
                }
            }
        }
        int maximum = dp[0].first;
        for (int i = 1; i < len; i++) 
            maximum = max(dp[i].first, maximum);
        int maxCount = 0;
        for (int i = 0; i < len; i++)
            if (dp[i].first == maximum) maxCount += dp[i].second;
        return maxCount;
    }
};
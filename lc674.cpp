class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        size_t len = nums.size();
        if (len == 0) return 0;
        int dp[len];
        dp[0] = 1;
        for (size_t i = 1; i < len; i++) {
            if (nums[i] > nums[i-1]) {
                dp[i] = dp[i-1] + 1;
            } else {
                dp[i] = 1;
            }
        }
        int maximum = dp[0];
        for (size_t i = 1; i < len; i++) 
            maximum = max(dp[i], maximum);
        return maximum;
    }
};
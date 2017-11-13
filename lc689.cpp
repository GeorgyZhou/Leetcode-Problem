class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        if (n < k * 3) return {};
        int sums[n - k + 1];
        sums[0] = accumulate(nums.begin(), nums.begin() + k, 0);
        for(int i = 1; i < n - k + 1; i++) {
            sums[i] = sums[i-1] + nums[i + k - 1] - nums[i-1];
        }
        vector<vector<int>> left(n - k + 1, vector<int>(2)), right(n - k + 1, vector<int>(2));
        left[0] = {sums[0], 0};
        right[n-k] = {sums[n-k], n-k};
        for(int i = 1; i < n - k + 1; i++) {
            if (sums[i] > left[i-1][0]) {
                left[i] = {sums[i], i};
            } else {
                left[i] = left[i-1];
            }
        }
        for(int i = n - k - 1; i >= 0; --i) {
            if (sums[i] >= right[i+1][0]) {
                right[i] = {sums[i], i};
            } else {
                right[i] = right[i+1];
            }
        }
        int curSum = 0;
        vector<int> res;
        for(int i = k; i < n - (k << 1) + 1; ++i) {
            if (sums[i] + left[i-k][0] + right[i+k][0] > curSum) {
                curSum = sums[i] + left[i-k][0] + right[i+k][0];
                res = {left[i-k][1], i, right[i+k][1]};
            }
        }
        return res;
        
    }
};
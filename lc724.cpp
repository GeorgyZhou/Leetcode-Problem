class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return -1;
        int sums[n];
        int sum = accumulate(nums.begin(), nums.end(), 0);
        for (int i = 0; i < nums.size(); i++) {
            sums[i] = i > 0 ? sums[i-1] + nums[i] : nums[i]; 
        }
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && sums[i-1] == sum - sums[i] || i == 0 && sum - sums[i] == 0) return i;
        }
        return -1;
    }
};
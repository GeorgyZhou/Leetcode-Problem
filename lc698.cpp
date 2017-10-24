class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) return false;
        int target = sum / k;
        sort(nums.begin(), nums.end(), greater<int>());
        vector<int> sets(k, target);
        return search(nums, sets, 0);
    }
private:
    bool search(vector<int> nums, vector<int> sets, int index) {
        if (index == nums.size()) {
            for (int i = 0; i < sets.size(); i++) {
                if (sets[i] != 0) return false;
            }
            return true;
        }
        for (int i = 0; i < sets.size(); i++) {
            if (nums[index] <= sets[i]) {
                sets[i] -= nums[index];
                if (search(nums, sets, index+1)) return true;
                sets[i] += nums[index];
            };
        }
        return false;
    }
};
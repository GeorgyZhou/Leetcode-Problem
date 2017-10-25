class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if (nums.size() < 4) return false;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 4 != 0) return false;
        int target = sum / 4;
        sort(nums.begin(), nums.end(), greater<int>());
        vector<int> sets(4, target);
        return search(nums, sets, 0);
    }
private:
    bool search(vector<int>& nums,vector<int>& sets, int index) {
        if (index == nums.size()) {
            for (int i = 0; i < 4; i++) {
                if (sets[i] != 0) return false;
            }
            return true;
        }
        for (int i = 0; i < 4; i++) {
            if (nums[index] > sets[i]) continue;
            sets[i] -= nums[index];
            if (search(nums, sets, index+1)) return true;
            sets[i] += nums[index];
        }
        return false;
    }
};
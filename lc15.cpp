class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end(), less<int>());
        for (int i = 0, r, l; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            l = i + 1;
            r = nums.size() - 1;
            while (l < r) {
                int s = nums[i] + nums[l] + nums[r];
                if (s < 0) l++;
                if (s > 0) r--;
                if (s == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l+1]) l++;
                    while (l < r && nums[r] == nums[r-1]) r--;
                    r--;
                    l++;
                }
            }
        }
        return res;
    }
};
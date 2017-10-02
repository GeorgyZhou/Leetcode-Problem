class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] <= nums[i+1]) continue;
            bool isPossible = false;
            if (i == 0 || nums[i+1] > nums[i-1])
                isPossible = (isPossible || check(nums, i+1));
            nums[i+1] = nums[i];
            isPossible = (isPossible || check(nums, i+1));
            return isPossible;
        }
        return true;
    }
private:
    bool check(vector<int>& nums, int start) {
        for (int i = start; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i+1]) return false;
        }
        return true;
    }
};
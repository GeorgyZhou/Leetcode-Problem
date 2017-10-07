class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int i;
        for (i = 0; i + 1< nums.size(); i += 2) {
            if (nums[i] != nums[i+1]) break;
        }
        return nums[i];
    }
};
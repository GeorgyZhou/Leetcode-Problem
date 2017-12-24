class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int sec = INT_MIN, largest = INT_MIN, ret = -1, num = 0;
        for (int i = 0; i < nums.size(); ++i) {
            num = nums[i];
            if (num >= largest) {
                sec = largest;
                largest = num;
                ret = i;
            } else if (num >= sec) {
                sec = num;
            }
        }
        return largest >= sec * 2 ? ret : -1;
    }
};
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        int start = 0, end = 0;
        int prod = 1, count = 0;
        while (end < nums.size()) {
            prod *= nums[end];
            while (prod >= k) prod /= nums[start++];
            end++;
            count += end - start;
        }
        return count;
    }
};
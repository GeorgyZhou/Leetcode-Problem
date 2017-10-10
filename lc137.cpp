class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a = 0, b = 0, ta;
        for (int& num : nums) {
            ta = (a & ~b & ~num) | (~a & b & num);
            b = (~a & b & ~num) | (~a & ~b & num);
            a = ta;
        }
        return a | b;
    }
};
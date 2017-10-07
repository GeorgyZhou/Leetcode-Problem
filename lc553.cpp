class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        stringstream ss;
        if (nums.size() < 3) {    
            for (int i = 0; i < nums.size(); i++) {
                if (i > 0) ss << "/"; 
                ss << nums[i];
            }
        } else {
            ss << nums[0] << "/";
            ss << "(";
            for (int i = 1; i < nums.size(); i++) {
                ss << nums[i];
                ss << (i == nums.size() - 1 ? ")" : "/");
            }
        }
        return ss.str();
    }
};
class Solution {
public:
    bool judgePoint24(vector<int>& nums) {
        vector<double> floats;
        for (int& num : nums) floats.push_back((double)num);
        return isValid(floats);
    }
private:
    bool isValid(vector<double>& nums) {
        // printVec(nums);
        if (nums.size() == 0) return false;
        if (nums.size() == 1) return (std::abs(nums[0] - 24) < 1e-6);
        for (int i = 0, j, k; i < nums.size(); i++) {
            for (j = 0; j < nums.size(); j++) {
                if (i == j) continue;
                vector<double> res;
                for (k = 0; k < nums.size(); k++) {
                    if (k == i || k == j) continue;
                    res.push_back(nums[k]);
                }
                for (k = 0; k < 4; k++) {
                    if (k < 2 && i > j) continue;
                    if (k == 0) res.push_back(nums[i] + nums[j]);
                    if (k == 1) res.push_back(nums[i] * nums[j]);
                    if (k == 2) res.push_back(nums[i] - nums[j]);
                    if (k == 3) {
                        if (nums[j] == 0) continue;
                        res.push_back(nums[i] / nums[j]);
                    }
                    if (isValid(res)) return true;
                    res.pop_back();
                }
            }
        }
        return false;
    }
    
    void printVec(vector<double> vec) {
        for (double& num : vec) {
            std::cout << num << " ";
        }
        std::cout << endl;
    }
};
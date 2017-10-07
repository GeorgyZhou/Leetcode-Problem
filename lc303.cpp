class NumArray {
public:
    NumArray(vector<int> nums) {
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                sums.push_back(nums[i]);
            } else {
                sums.push_back(sums[sums.size()-1] + nums[i]);
            }
        }
    }
    
    int sumRange(int i, int j) {
        return i != 0 ? sums[j] - sums[i-1] : sums[j];
    }
private:
    vector<int> sums;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */